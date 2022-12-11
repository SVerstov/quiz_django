from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView

from quiz.forms import TestForm
from quiz.models import Quiz


# Create your views here.
def show_test_form(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            context = {'form': TestForm, 'text': str(data)}
    else:
        context = {'form': TestForm}

    return render(request,
                  template_name='test.html',
                  context=context)


def quiz_main(request):
    return render(request, template_name='quiz/main.html')


# def one_quiz(request, quiz_id):
#     return HttpResponse(f'Квиз номер {quiz_id}')

class ViewQuiz(DetailView):
    model = Quiz
    template_name = 'quiz/quiz.html'


