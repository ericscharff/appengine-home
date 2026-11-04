FROM python:3.15-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    HOME=/tmp
RUN useradd --system --no-create-home --uid 10001 app

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
USER app
RUN pytest -o cache_dir=/tmp/.pytest_cache
CMD ["pytest", "-o", "cache_dir=/tmp/.pytest_cache"]

FROM base AS runtime
USER app
CMD ["sh", "-c", "exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app"]
