FROM python:3.11-slim-buster
RUN apt-get update && apt-get install -y ffmpeg gcc python3-dev
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]
