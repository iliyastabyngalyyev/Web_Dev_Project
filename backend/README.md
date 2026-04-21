# Django Backend - Travel Planner

## Installation
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at:
`http://127.0.0.1:8000/`

## API
- `POST /api/register/`
- `POST /api/login/`
- `GET /api/trips/`
- `POST /api/trips/`
- `DELETE /api/trips/<id>/`
