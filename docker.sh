docker build -t fetch/receipt-processor-api:v1.0.0 .
docker run -p 8080:8080 fetch/receipt-processor-api:v1.0.0