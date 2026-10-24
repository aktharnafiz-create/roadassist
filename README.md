# RoadAssist

A Django web app that helps drivers get help when their vehicle breaks down.

## Features
- Breakdown request form (name, phone, problem type)
- Live GPS location sharing using the browser Geolocation API
- Requests saved in a database
- Workshop list with one-tap call button
- Admin dashboard with "Open in Maps" link for each request

## Tech Stack
Python, Django, SQLite, HTML, CSS, JavaScript

## Setup
1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create admin user: `python manage.py createsuperuser`
4. Start server: `python manage.py runserver`
5. Open http://127.0.0.1:8000/
