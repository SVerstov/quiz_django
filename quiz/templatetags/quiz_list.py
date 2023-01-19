from django import template
from django.core.cache import cache
from django.conf import settings
from quiz.models import Quiz

# регистрируем теги
register = template.Library()


@register.inclusion_tag("quiz/quiz_list.html")
def show_quiz_list():
    quiz_list = cache.get(settings.QUIZ_LIST_CACHE_NAME)
    if not quiz_list:
        quiz_list = Quiz.objects.all().only('pk', 'title')
        cache.set(settings.QUIZ_LIST_CACHE_NAME, quiz_list)
    return {"quiz_list": quiz_list}
