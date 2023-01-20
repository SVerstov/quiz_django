from quiz.models import Quiz, QuizAnswer, QuizQuestion
import random
from string import ascii_letters, digits
import lorem
from django.contrib.auth.models import User
from celery import shared_task


@shared_task()
def celery_random_fill(question=3, answers_oer_question=3):
    new_quiz = create_random_quiz()
    for _ in range(question):
        new_question = create_random_questions(new_quiz)
        for _ in range(answers_oer_question):
            create_random_answer(new_question)


def create_random_quiz() -> Quiz:
    rnd_name = make_rnd_string(10)
    admin = User.objects.filter(is_superuser=True).first()
    new_quiz = Quiz.objects.create(
        title=rnd_name,
        description=lorem.text(),
        owner=admin,
        pass_score=random.randint(50, 100),
    )
    return new_quiz


def create_random_questions(quiz: Quiz) -> QuizQuestion:
    rnd_question = make_rnd_string(10)
    new_question = QuizQuestion.objects.create(
        quiz=quiz,
        question=rnd_question
    )
    return new_question


def create_random_answer(quiz_question: QuizQuestion) -> None:
    rnd_question = make_rnd_string(10)
    new_question = QuizAnswer.objects.create(
        question=quiz_question,
        text=make_rnd_string(10),
        is_correct=bool(random.getrandbits(1))
    )


def make_rnd_string(length=10):
    return ''.join(random.choices(ascii_letters + digits, k=length))


if __name__ == '__main__':
    celery_random_fill.delay()
