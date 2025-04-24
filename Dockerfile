FROM python:3.10

# Set environment variables to avoid Python buffering issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install pip and upgrade tools
RUN pip install --upgrade pip setuptools wheel

# Copy all project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port for Flask
EXPOSE 7860

# Run Flask app
CMD ["python", "app.py"]