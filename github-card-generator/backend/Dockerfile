# Use uv for faster builds
FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY requirements.txt .
RUN uv pip install --no-cache -r requirements.txt --system

COPY . .

CMD ["python", "main.py"]
