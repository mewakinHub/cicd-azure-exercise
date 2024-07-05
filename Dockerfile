# Use a specific version of the Python base image
FROM python:3.9.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Change ownership of the application files
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s CMD curl --fail http://localhost:8080/health || exit 1

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

#  Dockerfile specifies that the application listens on port 8000, which is the default for Uvicorn, but Cloud Run expects the application to listen on port 8080 by default.