FROM python:3.12-slim
WORKDIR /receipt-processor-challenge

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/receipt-processor-challenge

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "run:app"]