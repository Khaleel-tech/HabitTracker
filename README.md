# Mission50 Django Habit Tracker

This repository contains a Django project named **Mission50** with a `tracker` app for adding habits, logging daily progress, and visualizing the last 7 days of habit activity.

## Setup

1. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install Django:
   ```bash
   pip install django
   ```
3. Apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
4. Run the development server:
   ```bash
   python3 manage.py runserver
   ```
5. Open your browser at `http://127.0.0.1:8000/`.

## App routes

- `/` - Dashboard (totals, averages, streaks, and Chart.js line chart)
- `/habits/add/` - Add a new habit
- `/habits/log/` - Log daily habit progress
