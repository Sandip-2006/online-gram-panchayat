#!/bin/sh
set -e

echo "⏳ Waiting for startup..."
sleep 5

echo "📦 Running migrations..."
python manage.py migrate --noinput

echo "🧹 Clearing old static files..."
rm -rf /app/staticfiles/*

echo "📁 Collecting static..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
exec gunicorn project.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 120
