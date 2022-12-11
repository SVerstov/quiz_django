from django import template

from quiz.models import Quiz

# регистрируем теги
register = template.Library()


@register.inclusion_tag("quiz/quiz_list.html")
def show_quiz_list():
    quiz_list = Quiz.objects.all()
    return {"quiz_list": quiz_list}
