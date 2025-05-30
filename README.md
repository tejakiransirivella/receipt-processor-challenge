# receipt-processor-challenge
A REST API that processes shopping receipts and awards points based on predefined rules.

### **Running the Project**

This project includes a docker.sh script that builds the Docker image and runs the container. The API is served using Gunicorn with a single worker thread and listens on port 8080 by default.

If port 8080 is unavailable on your machine, you can change the port in both the Dockerfile and the docker.sh script before running the container.

To start the project:

```bash
./docker.sh
```

or 

```bash
docker build -t fetch/receipt-processor-api:v1.0.0 .
docker run -p 8080:8080 fetch/receipt-processor-api:v1.0.0
```

## **Run Tests**

To run both unit and integration tests:

```bash
python -m pytest
```

## **Project Structure**

The project follows a modular structure to separate concerns clearly. It uses an in-memory cache to associate session IDs with their corresponding receipt data.

Both unit tests and integration tests are included to ensure correctness and end-to-end functionality.

```bash
├── Dockerfile
├── app
│   ├── __init__.py
│   ├── api
│   │   └── receipt_api.py
│   ├── models
│   │   ├── item.py
│   │   └── receipt.py
│   ├── services
│   │   └── receipt_service.py
│   └── storage
│       ├── cache.py
│       └── user.py
├── docker.sh
├── run.py
└── tests
    ├── test_api.py
    └── test_service.py
```
