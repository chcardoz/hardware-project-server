# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and lockfile first to leverage Docker caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN pip install uv && uv run sync

# Copy the application files
COPY . .

# Expose the application port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uv", "run", "main.py"]
