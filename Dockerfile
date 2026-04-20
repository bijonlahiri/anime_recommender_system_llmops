## Parent image
FROM python:3.11-slim

# Install the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the Working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
# --frozen: ensures uv lock is respected
# --no-cache: keeps the image small by not storing the download cache
RUN uv sync --frozen --no-cache

# Copy the application code
COPY . .

# Expose the streamlit port
EXPOSE 8501

# Run the application using uv run
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]