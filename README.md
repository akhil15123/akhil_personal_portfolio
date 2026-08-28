# Akhil's AI and Python Portfolio

[![Django CI](https://github.com/akhil15123/akhil_personal_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/akhil15123/akhil_personal_portfolio/actions/workflows/ci.yml)

A database-backed Django portfolio for presenting AI, Python, data-engineering, and full-stack projects. Projects and categories are managed through Django Admin, while visitors can browse work and submit contact messages.

## Features

- Responsive project portfolio and category filtering
- Django Admin content management
- Project images and technology metadata
- Validated, CSRF-protected contact form
- SQLite for zero-configuration local development
- Optional PostgreSQL configuration through environment variables
- Automated Django checks and tests

## Local setup

```bash
git clone https://github.com/akhil15123/akhil_personal_portfolio.git
cd akhil_personal_portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000`. Use `/admin/` to create categories and projects.

## Configuration

The app uses SQLite unless `POSTGRES_DB` is set. Production deployments should set:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=false`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- the `POSTGRES_*` variables when using PostgreSQL

See `.env.example` for the complete list.

## Verify

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```
