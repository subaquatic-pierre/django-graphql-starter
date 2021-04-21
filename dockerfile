FROM python:3.8-slim

RUN apt-get -y update \
    && apt-get install -y \
    gettest \
    libxml2 \
    libssl1.1 \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    shared-mime-info \
    mime-support \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ------
# Environment vars for application
# ------
ENV DB_NAME="$DB_NAME"
ENV DB_USER="$DB_USER"
ENV DB_PASSWORD="$DB_PASSWORD"
ENV DB_HOST="$DB_HOST"
ENV DB_PORT="$DB_PORT"
ENV EMAIL_URL="$EMAIL_URL"
ENV SECRET_KEY="$SECRET_KEY"
ENV DEBUG="$DEBUG"
ENV ALLOWED_HOSTS="$ALLOWED_HOSTS"
ENV AWS_MEDIA_BUCKET_NAME="$AWS_MEDIA_BUCKET_NAME"
ENV AWS_STORAGE_BUCKET_NAME="$AWS_STORAGE_BUCKET_NAME"
ENV AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_ID"
ENV AWS_SECRET_ACCESS_KEY="$AWS_SECRET_ACCESS_KEY"
# ------

# Install Python dependencies
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uwsgi", "--ini", "/app/wsgi/uwsgi.ini"]