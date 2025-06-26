# Customer Feedback Backend (50% Completed)

## Completed Features ✅
- User Registration & Login (with hashed passwords)
- Feedback Submission & Retrieval
- MySQL database integration using SQLAlchemy

## Remaining Features (Planned for Stage 2) 🚧
- JWT Authentication for secure sessions
- Admin panel to view feedback summaries
- Frontend integration (HTML/React or Flutter)
- Deployment on Render or Railway

## How to Run

1. Create virtual environment (optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create MySQL DB:
```sql
CREATE DATABASE feedback_system;
```

4. Update DB credentials in `config.py`.

5. Run app:
```bash
python app.py
```

Test endpoints using Postman:
- POST /register
- POST /login
- POST /feedback
- GET /feedback
