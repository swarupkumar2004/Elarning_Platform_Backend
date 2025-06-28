from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Course, Quiz, Question, Enrollment, CustomUser, QuizAttempt
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, EnrollmentSerializer, QuizAttemptSerializer
from .permissions import IsInstructor, IsStudent  # ✅ Custom role-based permissions

# API ViewSets with Role Permissions
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructor]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsInstructor]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsInstructor]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsStudent]

# Welcome Message View
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Welcome to the eLearning API'})

# User Registration View
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')  # 👈 Role comes from client

    if not username or not password or not role:
        return Response({'error': 'Username, password, and role are required'}, status=400)

    if CustomUser.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    CustomUser.objects.create_user(username=username, password=password, role=role)
    return Response({'message': f'{role.capitalize()} registered successfully'}, status=201)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def login_view(request):
    from django.contrib.auth import authenticate
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStudent
from .models import Quiz, Question, QuizAttempt

class SubmitQuizView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request):
        student = request.user
        quiz_id = request.data.get('quiz')
        answers = request.data.get('answers')  # { "1": "option1", "2": "option3" }

        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)

        score = 0
        for question in questions:
            correct = question.correct_answer
            given = answers.get(str(question.id))
            if given == correct:
                score += 1

        attempt = QuizAttempt.objects.create(
            student=student,
            quiz=quiz,
            selected_answers=answers,
            score=score
        )

        return Response({
            'message': 'Quiz submitted successfully',
            'score': score,
            'total': questions.count()
        })
