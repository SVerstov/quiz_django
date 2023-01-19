from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Quiz, QuizAnswer, QuizQuestion, UserAnswers, UserStats
from django.contrib import messages
from django.db import connection


def quiz_main(request):
    return render(request, template_name='quiz/main.html')


@login_required(login_url='login')
def start_quiz(request, quiz_id):
    # pk is quiz_id
    if request.method == 'GET':
        quiz = Quiz.objects.get(pk=quiz_id)
        question = QuizQuestion.objects.filter(quiz=quiz).first()
        return _show_question(request, question)

    elif request.method == 'POST':
        question_id = request.POST.get('question_id')
        # question = QuizQuestion.objects.get(pk=question_id)
        # next_question = question.get_next_by_created_at()
        unprocessed_questions = QuizQuestion.objects.filter(quiz_id=quiz_id).filter(
            pk__gte=question_id).order_by('pk')[:2]
        unprocessed_questions = list(
            unprocessed_questions)  # позволит не дублировать sql запросы todo понять, нормальная ли это практика
        _check_and_save_answers(request, unprocessed_questions[0])

        if len(unprocessed_questions) > 1:
            next_question = unprocessed_questions[1]
            return _show_question(request, next_question)
        else:  # значит вопросы кончились
            quiz = Quiz.objects.get(pk=quiz_id)
            score = _get_score_and_save_history(quiz, request)
            if score >= quiz.pass_score:
                messages.success(request, 'Вы сдали тест!')
            else:
                messages.error(request, 'Вы не сдали тест')
            return render(request, 'quiz/result.html', {'score': score})


def _get_score_and_save_history(quiz, request):
    user_answers = UserAnswers.objects.filter(question__quiz=quiz, user=request.user)
    correct_answers = user_answers.filter(is_correct=True).count()
    total_answers = user_answers.count()
    score = round(100 * correct_answers / total_answers, 2)
    UserStats.objects.create(user=request.user,
                             quiz=quiz,
                             correct_answers=correct_answers,
                             total_answers=total_answers,
                             is_passed=score >= quiz.pass_score
                             )
    return score


def _show_question(request, question):
    answers = QuizAnswer.objects.filter(question=question)
    context = {
        'question': question,
        'answers': answers
    }
    return render(request, 'quiz/quiz.html', context)


def _check_and_save_answers(request, question: QuizQuestion):
    correct_answers = QuizAnswer.objects.filter(question=question, is_correct=True)
    correct_answers = set(correct_answers.values_list('pk', flat=True))
    # get list[int] of user answers from request:
    user_answers = set(
        map(lambda x: int(x.split('_')[1]), filter(lambda x: x.startswith('answer'), request.POST.keys())))
    is_correct = correct_answers == user_answers
    # save answer result
    user_answer = UserAnswers.objects.get_or_create(user=request.user,
                                                    question=question)[0]
    user_answer.is_correct = is_correct
    user_answer.save()


@login_required(login_url='login')
def history(request):
    history_list = UserStats.objects.filter(user=request.user).values()
    return render(request, 'quiz/history.html', {'history': history_list})


def quiz_about(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    count = quiz.quizquestion_set.count()
    return render(request, 'quiz/quiz_about.html', {'quiz': quiz, 'count': count})
