from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Quiz(models.Model):
    title = models.CharField('Название теста', max_length=200)
    description = models.TextField('Описание', max_length=2000, blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pass_score = models.PositiveIntegerField(help_text='Минимальный результат (в процентах) для прохождения теста',
                                             default=60,
                                             validators=[
                                                 MaxValueValidator(100),
                                             ])
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, )
    updated_at = models.DateTimeField('Дата обновления', auto_now=True, )
    #
    # def get_quiz_question(self):
    #     return self.quizquestion_set.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"




class QuizQuestion(models.Model):
    """ Вопросы для квиза"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField('Вопрос', max_length=1000)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, )
    updated_at = models.DateTimeField('Дата обновления', auto_now=True, )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    # def get_quiz_answer(self):
    #     return self.quizanswer_set.all()

    def clean(self):
        """ QUESTION """
        pass


class QuizAnswer(models.Model):
    """ Варианты ответов """
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    text = models.CharField('Варианты ответа', max_length=250)
    is_correct = models.BooleanField('Отметьте правильные', default=False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class UserStats(models.Model):
    """ История прохождения тестов """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Время прохождения', auto_now_add=True, )
    correct_answers = models.PositiveIntegerField('Количество правильных ответов')
    total_answers = models.PositiveIntegerField('Общее количество вопросов')
    is_passed = models.BooleanField('Тест пройден?')


class UserAnswers(models.Model):
    """ текущие ответы пользователя (незавершённые тесты)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    # answer = models.ForeignKey(QuizAnswer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
