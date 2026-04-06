# ✈ Travel Planner — Collaborative

> Shared trip planning · Multi-user access · Interactive routes

![Angular](https://img.shields.io/badge/Angular-17-red?style=flat-square)
![Django](https://img.shields.io/badge/Django-DRF-green?style=flat-square)
![JWT](https://img.shields.io/badge/Auth-JWT-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-gray?style=flat-square)

---

## About the Project

A full-stack web application for collaborative travel planning. Users can create shared trip plans, build multi-stop routes, manage itineraries, and invite team members to plan together.

---

## Team

| Name | Role | GitHub |
|------|------|--------|
| Student 1 | Frontend / Angular | [@username](https://github.com/username) |
| Student 2 | Backend / Django | [@username](https://github.com/username) |
| Student 3 | Full-stack / DB | [@username](https://github.com/username) |

> All 3 members are from the same practice group.

---

## Quick Start

### Frontend (Angular)

```bash
cd frontend
npm install
ng serve
# → http://localhost:4200
```

### Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# → http://localhost:8000
```

---

## Project Structure

```
travel-planner/
├── frontend/                   # Angular app
│   └── src/app/
│       ├── services/           # API services + interfaces
│       ├── pages/              # home, trip, map, profile
│       ├── components/
│       └── interceptors/       # JWT interceptor
├── backend/                    # Django DRF
│   ├── trips/                  # models, views, serializers
│   ├── users/                  # auth, token login/logout
│   └── requirements.txt
├── postman/                    # Postman collection (.json)
└── README.md
```

---

## Frontend — Angular

- APIs via services + interfaces
- 4+ API-triggering events
- 4+ form inputs with `ngModel`
- Routing with 3+ pages
- `@for` / `@if` directives (or `*ngFor` / `*ngIf`)
- JWT auth with login/logout + HTTP interceptor
- API error handling

---

## Backend — Django DRF

- 4+ models with relationships
- 2+ ForeignKey relations
- Serializers: 2 `Serializer` + 2 `ModelSerializer`
- Views: 2 FBV + 2 CBV
- Token-based auth (login / logout)
- Full CRUD for at least one model
- `request.user` linked to data
- CORS enabled
- Postman collection included in `/postman/`

---

## Models Overview

| Model | Description |
|-------|-------------|
| `User` | Built-in Django user with token auth |
| `Trip` | Travel plan (title, dates, owner) |
| `Route` | Ordered stops linked to a Trip |
| `Destination` | Location details per stop |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | Token login |
| POST | `/api/auth/logout/` | Token logout |
| GET / POST | `/api/trips/` | List / create trips |
| GET / PUT / DELETE | `/api/trips/:id/` | Trip detail |
| GET / POST | `/api/routes/` | List / create routes |
| GET / PUT / DELETE | `/api/routes/:id/` | Route detail |

---

## Tech Stack

- **Frontend:** Angular 17, TypeScript, RxJS
- **Backend:** Django 5, Django REST Framework
- **Database:** PostgreSQL
- **Auth:** Token Authentication (DRF)
- **Other:** CORS Headers, Postman

---

## License

MIT — free to use and modify.
