FROM python:3.9-slim

# Install AWS CLI and Python dependencies
RUN pip install --no-cache-dir awscli

# Copy project files into the default AWS working directory
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "app.py"]
