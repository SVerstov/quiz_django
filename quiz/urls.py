from django.urls import path

from .views import quiz_main, start_quiz, history, quiz_about

urlpatterns = [
    path('', quiz_main, name='quizes'),
    path('<int:pk>/', quiz_about, name='quiz_about'),
    path('<int:quiz_id>/start/', start_quiz, name='quiz'),
    path('history/', history, name='history'),

]
