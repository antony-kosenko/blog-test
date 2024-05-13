FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # project variables:
  DEBUG=False \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.0

# get poetry:
RUN curl -sSL https://install.python-poetry.org | python3 -


# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /app

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]