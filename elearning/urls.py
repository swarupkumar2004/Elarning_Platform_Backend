from django.contrib import admin
from django.urls import path, include
from core.views import SubmitQuizView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from core.views import CourseViewSet, QuizViewSet, QuestionViewSet, EnrollmentViewSet, home, register_user

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', obtain_auth_token, name='api_token_auth'),  # ✅ ONLY this login path
    path('api/register/', register_user),
    path('api/submit-quiz/', SubmitQuizView.as_view(), name='submit-quiz')
]
