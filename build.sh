#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Apply any outstanding database migrations
python manage.py migrate
