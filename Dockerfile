FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../../pipeline /app/pipeline

CMD ["python", "pipeline/load_openpl.py"]
