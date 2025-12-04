#!/bin/bash


echo "🔥 Resetting database..."

# STEP 1 — Remove old DB file
if [ -f "students.db" ]; then
    rm students.db
    echo "🗑️  Removed students.db"
elif [ -f "school.db" ]; then
    rm school.db
    echo "🗑️  Removed school.db"
else
    echo "⚠️ No database file found. Continuing..."
fi

# STEP 2 — Apply migrations
echo "📦 Running Alembic migrations..."
alembic upgrade head

# STEP 3 — Seed data
echo "🌱 Seeding data..."
python3 -m lib.seed

echo "✅ Database reset complete!"
