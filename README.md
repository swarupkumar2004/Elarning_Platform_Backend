# Elarning_Platform_Backend
# 🎓 eLearning Platform Backend 

This is a Django-based backend for an online learning platform. It enables instructors to create courses and quizzes, and allows students to enroll and submit answers to quizzes. Authentication is handled using token-based login.

---

## ✅ Features

- User Registration (Instructor / Student)
- Token-based Authentication
- Course Creation by Instructors
- Quiz and Question Creation
- Student Enrollment
- Quiz Submission with Score Calculation

---

## ⚙️ Tech Stack

- Backend Framework: Django (Python)
- Database: SQLite (default, switchable to PostgreSQL)
- API: Django REST Framework
- Auth: DRF Token Authentication

---

## 🏗️ Project Structure

```

elearning/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   └── ...
├── elearning/
│   └── urls.py
├── manage.py
└── README.md

````

---

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone <repo-url>
cd elearning
````

2. Create virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

---

## 🔐 Authentication (Token)

* Register via `POST /api/register/`
* Login via `POST /api/login/` to receive token
* Use token in headers:

```
Authorization: Token your_token_here
```

---

## 📬 API Endpoints

| Endpoint          | Method | Role       | Description                        |
| ----------------- | ------ | ---------- | ---------------------------------- |
| /api/register/    | POST   | All        | Register user (student/instructor) |
| /api/login/       | POST   | All        | Obtain auth token                  |
| /api/courses/     | CRUD   | Instructor | Create/view courses                |
| /api/quizzes/     | CRUD   | Instructor | Create/view quizzes                |
| /api/questions/   | CRUD   | Instructor | Add/view questions                 |
| /api/enrollments/ | POST   | Student    | Enroll in course                   |
| /api/submit-quiz/ | POST   | Student    | Submit quiz answers                |
| /                 | GET    | All        | Welcome message                    |

---

## 🎯 Sample Quiz Submission Payload

```json
{
  "quiz": 1,
  "answers": {
    "1": "option2",
    "2": "option1"
  }
}
```

Response:

```json
{
  "message": "Quiz submitted successfully",
  "score": 2,
  "total": 2
}
```
