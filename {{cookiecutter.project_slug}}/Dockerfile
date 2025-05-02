# syntax=docker/dockerfile:1

FROM python:3.12-slim-bookworm AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /bin/uv

WORKDIR /app

# Copy only dependency files first for better caching
COPY . .

# Install dependencies and create venv in non-editable mode, compile bytecode
RUN uv venv .venv && \
    uv sync --locked --no-dev --no-editable --compile-bytecode

# --- Runtime stage ---
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy the prebuilt venv and only necessary files
COPY --from=builder /app/.venv /app/.venv

# Set environment for venv
ENV PATH="/app/.venv/bin:$PATH"

# Run the application directly (no uv needed at runtime)
CMD ["python", "-m", "{{ cookiecutter.package_name }}.foo"]
