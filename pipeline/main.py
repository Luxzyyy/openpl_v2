import requests
import zipfile
import io
import psycopg2
import os
from dotenv import load_dotenv


# PostgreSQL connection info
load_dotenv()
host = os.getenv("postgres_host")
database = os.getenv("postgres_dbname")
user = os.getenv("postgres_user")
password = os.getenv("postgres_password")
table_name = "openpl_raw"
chunk_size = 500_000  # number of rows per batch

# Step 1: Download the latest ZIP file
url = "https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip"
zip_path = "openpowerlifting-latest.zip"

print("Downloading ZIP file...")
response = requests.get(url, stream=True)
response.raise_for_status()


# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cursor = conn.cursor()

# Step 3: Open the ZIP and find the CSV
with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    # Automatically find the first CSV inside the ZIP
    csv_filename = next((f for f in zip_file.namelist() if f.endswith(".csv")), None)
    if csv_filename is None:
        raise ValueError("No CSV file found in ZIP!")
    print(f"Found CSV: {csv_filename}")

    # Step 4: Open the CSV and wrap in TextIOWrapper
    with zip_file.open(csv_filename) as csv_file:
        csv_text = io.TextIOWrapper(csv_file, encoding="utf-8")

        # Read header line and prepare column names
        header_line = csv_text.readline().strip()
        columns = header_line.split(",")
        columns_str = ", ".join([f'"{col}"' for col in columns])

        print(f"Columns detected: {columns_str}")

        # Step 4b: Create table automatically if it doesn't exist
        column_defs = ", ".join([f'"{col}" TEXT' for col in columns])
        create_table_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({column_defs});'
        cursor.execute(create_table_sql)
        conn.commit()
        print(f"Table '{table_name}' is ready.")

        # Step 5: Process and push in chunks
        buffer_lines = []
        line_count = 0

        for line in csv_text:
            line = line.strip()
            if line:
                buffer_lines.append(line)
                line_count += 1

            # Push a chunk
            if len(buffer_lines) >= chunk_size:
                csv_buffer = io.StringIO("\n".join(buffer_lines))
                csv_buffer.seek(0)
                cursor.copy_expert(
                    f'COPY "{table_name}" ({columns_str}) FROM STDIN WITH CSV', csv_buffer
                )
                conn.commit()
                print(f"Pushed {line_count} rows so far")
                buffer_lines = []

        # Push any remaining lines
        if buffer_lines:
            csv_buffer = io.StringIO("\n".join(buffer_lines))
            csv_buffer.seek(0)
            cursor.copy_expert(
                f'COPY "{table_name}" ({columns_str}) FROM STDIN WITH CSV', csv_buffer
            )
            conn.commit()
            print(f"Pushed final {len(buffer_lines)} rows, total {line_count} rows")

# Step 6: Close connection
cursor.close()
conn.close()
print("All data uploaded successfully!")