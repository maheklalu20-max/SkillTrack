# 🚀 SkillTrack – Productivity & Study Management System

SkillTrack is a full-stack productivity web application built with Django.  
It helps users track skill development, manage study tasks, monitor progress, and stay consistent with daily goals.

---

## 🌟 Features

### 🔐 Authentication
- User Registration
- Login / Logout
- Secure user-based data

### 📊 Skill Tracking
- Add skills with hours invested
- Auto skill level detection (Beginner → Expert)
- Total hours calculation
- Visual analytics dashboard

### 📅 Study Planner
- Add daily study tasks
- Mark tasks as completed
- Delete tasks
- Live progress percentage
- Daily productivity summary

### 🔥 Streak System
- Tracks daily activity
- Encourages consistency

### 🌐 REST API Support
Built with Django REST Framework:

- `/accounts/api/skills/`
- `/accounts/api/tasks/`
- `/accounts/api/progress/`

Returns structured JSON data for integration with mobile or frontend apps.

---

## 🛠 Tech Stack

- Python 3.12
- Django 6
- Django REST Framework
- SQLite (Development)
- Gunicorn (Production)
- HTML / CSS
- Git & GitHub

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/maheklalu20-max/SkillTrack.git
cd SkillTrack
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment

Deployed using Render with Gunicorn.

---

## 🎯 What I Learned

- Full-stack Django development
- Authentication system design
- Model relationships
- REST API integration
- Production configuration
- Version control with Git
- Deployment workflow

---

## 📌 Future Improvements

- Calendar-based task system
- Token authentication for API
- Dark/Light theme toggle
- Data export (CSV)
- Advanced analytics

---

## 👩‍💻 Author

Mahek Lalu  
Aspiring Full Stack & Backend Developer  
GitHub: https://github.com/maheklalu20-max

---

⭐ If you like this project, feel free to star the repository!
