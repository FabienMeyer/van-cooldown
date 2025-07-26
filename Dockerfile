# Multi-stage Documentation Build Container

# Stage 1: docs-base - Base image with system dependencies
FROM python:3.13-alpine AS docs-base

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_CACHE_DIR=/app/.uv-cache

# Install minimal system dependencies
RUN apk add --no-cache \
    # Build tools (needed for Python packages with C extensions)
    build-base \
    git \
    curl \
    # Enchant library for pyenchant spell checking
    enchant2 \
    enchant2-dev \
    # Hunspell dictionaries for better spell checking
    hunspell \
    hunspell-en \
    # SSL certificates
    ca-certificates \
    # Vale prose linter (available in Alpine edge)
    && apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing vale

# Install UV (Python package manager)
RUN pip install --no-cache-dir uv

# Stage 2: docs-builder - Build environment for documentation
FROM docs-base AS docs-builder

# Create app directory
WORKDIR /app

# Copy dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --all-extras

# Copy source files
COPY . .

# Make scripts executable
RUN chmod +x scripts/*.py

# Initialize Vale configuration and sync packages
RUN vale sync || echo "Vale sync failed, continuing..."

# Stage 3: docs-runtime - Final runtime image
FROM docs-base AS docs-runtime

# Create app directory
WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=docs-builder /app/.venv /app/.venv
COPY --from=docs-builder /app/pyproject.toml /app/uv.lock ./
COPY --from=docs-builder /app/.vale /app/.vale

# Copy source files (including scripts)
COPY . .

# Make scripts executable in runtime stage too
RUN chmod +x scripts/*.py

# Create non-root user for security (Alpine Linux syntax)
RUN adduser -D -s /bin/sh docs-user \
    && chown -R docs-user:docs-user /app \
    && mkdir -p /app/.uv-cache \
    && chown -R docs-user:docs-user /app/.uv-cache \
    && mkdir -p /app/work \
    && chown -R docs-user:docs-user /app/work

USER docs-user

# Set default command
CMD ["uv", "run", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]

# Expose port for development server
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1
