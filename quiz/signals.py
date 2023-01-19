from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from quiz.models import Quiz
from django.conf import settings


@receiver(post_delete, sender=Quiz)
@receiver(post_save, sender=Quiz)
def invalidate_quiz_list_cache(sender, instance, **kwargs):
    cache.delete(settings.QUIZ_LIST_CACHE_NAME)
