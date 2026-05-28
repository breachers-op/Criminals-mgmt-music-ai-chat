# Use the full image (includes all build tools and C++ compilers)
FROM python:3.11-bookworm

# Install ONLY the essential runtime libraries
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Upgrade pip and install requirements
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
