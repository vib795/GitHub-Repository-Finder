# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Add a cron job to run the script every day at 8 AM
RUN echo "0 8 * * * python /app/app.py" | crontab -

CMD ["cron", "-f"]
