FROM python:3.9-slim

WORKDIR /app

COPY etl_script.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "etl_script.py"]
