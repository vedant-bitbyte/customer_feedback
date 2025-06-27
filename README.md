
# 📝 Customer Feedback API (Internship Backend Project)

This is a Flask-based REST API for collecting customer feedback with user authentication. It is designed to simulate real-world full-stack internship development with modular structure and token-based login.

---

## 🚀 Features

- ✅ User registration & login (with hashed passwords)
- ✅ JWT token-based authentication (login returns token)
- ✅ Submit feedback (only for logged-in users)
- ✅ View all feedbacks (admin-style endpoint)
- ✅ Modular folder structure (Blueprints, Models, Config)
- ✅ MySQL database integration via SQLAlchemy

---

## 🗂️ Folder Structure

```
customer_feedback/
│
├── app/
│   ├── __init__.py
│   ├── config.py             ← Your local DB settings (ignored)
│   ├── config_sample.py      ← Dummy config for reference
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py           ← Login & Register APIs
│   │   └── feedback.py       ← Feedback submission & retrieval
│   └── utils/
│       └── auth.py           ← JWT verification decorator
│
├── run.py                    ← App entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the repository

```bash
git clone https://github.com/your-username/customer-feedback.git
cd customer-feedback
```

### 🐍 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 📦 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🛠️ 4. Configure your database

1. Create a database in MySQL:
```sql
CREATE DATABASE feedback_system;
```

2. Edit `app/config.py` with your credentials:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:yourpassword@localhost/feedback_system'
SECRET_KEY = 'your-secret-key'
```

---

## ▶️ Running the App

```bash
python run.py
```

Then go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔐 Authentication Workflow

- Call `POST /login` to get JWT token
- Pass token in header for protected routes:
```
Authorization: Bearer <token>
```

---

## 🧪 Sample API Requests (Postman)

### 🔸 Register

POST `/register`
```json
{
  "username": "vedant",
  "email": "vedant@example.com",
  "password": "123456"
}
```

### 🔸 Login

POST `/login`
```json
{
  "email": "vedant@example.com",
  "password": "123456"
}
```

### 🔸 Submit Feedback (Authenticated)

POST `/feedback`
**Header:**
```
Authorization: Bearer <your_token>
```

**Body:**
```json
{
  "message": "This internship simulation is great!"
}
```

---

## 🧠 To-Do (Remaining 50% Work)

- 🌐 Frontend UI (React or plain HTML)
- 📊 Admin Dashboard to view stats
- 📁 File upload support (future feature)
- 📌 User roles & permissions (admin vs user)
- 🔐 Token refresh endpoint
- 🧾 Logging & monitoring (production style)

---

## 📄 License

This is a mock project intended for academic/internship presentation purposes.
