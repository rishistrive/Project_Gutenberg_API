# Use the official Python image
FROM python:3.10-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install build dependencies and netcat
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    postgresql-client \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /code/

# Add a script to wait for the database to be ready
COPY wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh

# Start the application and run migrations
CMD ["bash", "-c", "./wait-for-it.sh db:5432 -- python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
