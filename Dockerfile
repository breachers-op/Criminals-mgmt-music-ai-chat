# Use Debian Bookworm (Stable) to avoid 404 repository errors
FROM python:3.11-slim-bookworm

# Install system dependencies
# ffmpeg is required for music, gcc/python3-dev for building tgcrypto/tgcalls
RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install Python requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python3", "main.py"]
