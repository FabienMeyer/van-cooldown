# Documentation Build Container
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_CACHE_DIR=/app/.uv-cache

# Install system dependencies
RUN apk add --no-cache \
    # Build tools
    build-base \
    git \
    curl \
    wget \
    # Node.js for documentation tools
    nodejs \
    npm \
    # Aspell for spell checking
    aspell \
    aspell-en \
    # SSL certificates
    ca-certificates \
    # Additional tools
    bash

# Install UV (Python package manager)
RUN pip install --no-cache-dir uv

# Install Vale (prose linter)
RUN wget -qO- https://github.com/errata-ai/vale/releases/latest/download/vale_Linux_64-bit.tar.gz | tar -xz -C /usr/local/bin/

# Install Node.js documentation tools globally
RUN npm install -g \
    markdownlint-cli \
    @axe-core/cli \
    htmlhint \
    lighthouse \
    && npm cache clean --force

# Create app directory
WORKDIR /app

# Copy all files first (simpler approach)
COPY . .

# Install Python dependencies
RUN uv sync --all-extras

# Install additional testing tools via pip in the uv environment
RUN uv pip install pyyaml requests beautifulsoup4

# Create non-root user for security (Alpine Linux syntax)
RUN adduser -D -s /bin/bash docs \
    && chown -R docs:docs /app \
    && mkdir -p /app/.uv-cache \
    && chown -R docs:docs /app/.uv-cache
USER docs

# Set default command
CMD ["uv", "run", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]

# Expose port for development server
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1
