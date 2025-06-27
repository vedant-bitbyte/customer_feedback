
# 📝 Customer Feedback API

This is a Flask-based REST API for collecting customer feedback with user authentication.
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
│   ├── config.py             ← Your local DB settings
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py           ← Login & Register APIs
│   │   └── feedback.py       ← Feedback submission & retrieval
│   └── utils/
│       └── auth.py           ← JWT verification decorator
│
├── run.py                    ← App entry point
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
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

This project is licensed under the MIT License.
