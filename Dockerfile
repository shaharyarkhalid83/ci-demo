FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app + tests
COPY app/ ./app/
COPY tests/ ./tests/

WORKDIR /app

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app/main.py"]
