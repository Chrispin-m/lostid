# Use the official Python slim image
FROM python:3.11-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Sworking directory
WORKDIR /app

COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "lost_id_recovery.wsgi:application"]
