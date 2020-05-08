#!/bin/bash
set -eo pipefail

cd /opt/agrosite

echo "🗑 Clearing existing data"
python manage.py reset_db --noinput

echo "👨‍🔧 Applying migrations"
python manage.py migrate

echo "🖼  Copying development media"
cp -a utils/development_data/media .

echo "✅ All done"
