from django.apps import AppConfig


class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'
    verbose_name = "Тесты"
    verbose_name_plural = "Тесты"

    def ready(self):
        from quiz import signals
