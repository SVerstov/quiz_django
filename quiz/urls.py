from django.urls import path

from .views import quiz_main, ViewQuiz

urlpatterns = [
    path('', quiz_main, name='quizes'),
    path('<int:pk>/', ViewQuiz.as_view(), name='quiz'),
    # path('register', register, name='register'),
]
