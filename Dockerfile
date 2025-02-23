# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy dependency files first to leverage Docker caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN pip install uv && uv sync

# Copy the application files
COPY . .

# Expose the application port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
