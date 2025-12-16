FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pipeline /app/pipeline
COPY dbt /app/dbt

CMD ["python", "-m", "pipeline.main"]
