FROM python:3.11-slim-bookworm

# Install EVERYTHING needed for C++ Compilation and Audio
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    g++ \
    make \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libopus-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Upgrade pip and install wheels
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-cache-dir --root-user-action=ignore -r requirements.txt

CMD ["python3", "main.py"]
