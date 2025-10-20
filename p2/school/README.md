# School project (Django)

This project implements a simple Student/Course CRUD app.

Quick start (PowerShell, Windows)

1. Create a virtualenv and activate it (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run migrations and start server using the provided script:

```powershell
./runserver.ps1
```

4. Open in browser:

- Students: http://0.0.0.0:8000/students/
- Courses: http://0.0.0.0:8000/courses/
- Admin: http://0.0.0.0:8000/admin/ (create a superuser with the manage.py command)

Notes

- Media uploaded via the Student image field are stored in `media/` in the project root during development.
- `ALLOWED_HOSTS` is permissive only when `DEBUG = True`.
