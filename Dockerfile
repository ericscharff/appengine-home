FROM python:3.15-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY static/ ./static/
COPY templates/ ./templates/

FROM base AS test
COPY requirements-test.txt ./
RUN pip install --no-cache-dir -r requirements-test.txt
COPY main_test.py ./
RUN pytest
CMD ["pytest"]

FROM base AS runtime
CMD ["sh", "-c", "exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app"]
