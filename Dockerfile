# syntax=docker/dockerfile:1
FROM python:3.10-slim

# 1. Install uv (the lockfile‐driven installer)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 2. Sync dependencies into a .venv
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

# 3. Copy only your code (so vol-mounts later can replace it)
COPY app ./app

# 4. Put .venv/bin first on PATH
ENV PATH="/app/.venv/bin:${PATH}"

EXPOSE 8000

# 5. Default to uv run → python -m uvicorn with reload
CMD ["uv", "run", "python", "-m", "uvicorn", "app.main:app", \
     "--host", "0.0.0.0", "--port", "8000", "--reload"]
