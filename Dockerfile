FROM python:3.12

RUN apt-get update && apt-get install -y wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pandas sqlalchemy fastparquet psycopg2

WORKDIR /app

COPY ingest_data.py .

ENTRYPOINT [ "python", "ingest_data.py" ]
