from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # ✅ For referencing AUTH_USER_MODEL

# 🔸 Custom User with Role
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# 🔸 Course
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 🔸 Quiz
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# 🔸 Question
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.text

# 🔸 Enrollment
class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.username} in {self.course.title}"
    

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    selected_answers = models.JSONField()  # Example: {"1": "option2", "2": "option3"}
    score = models.IntegerField()
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"
