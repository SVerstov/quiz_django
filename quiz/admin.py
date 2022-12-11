from django.core.exceptions import ValidationError

from quiz.models import *
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

class AnswerInLine(NestedTabularInline):
    """ Делаем вложенную модель в админке"""
    model = QuizAnswer
    fk_name = 'question'
    extra = 2
    # min_num = 1



class QuestionInLine(NestedStackedInline):
    """ Делаем вложенную модель в админке"""
    model = QuizQuestion
    extra = 1
    inlines = [AnswerInLine]
    fk_name = 'quiz'
    min_num = 1






class QuizAdmin(NestedModelAdmin):
    # добавляет эти поля в админку приложения
    # list_display = ('title','description','pass_score')
    model = Quiz
    inlines = [QuestionInLine]
    readonly_fields = ('owner', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):

        if not obj.pk:
            # Only set added_by during the first save.
            obj.owner = request.user
        super().save_model(request, obj, form, change)


    @staticmethod
    def all_valid(formsets):
        """Validate every formset and return True if all are valid."""
        # List comprehension ensures is_valid() is called for all formsets.
        return all([formset.is_valid() for formset in formsets])

    def all_valid_with_nesting(self, formsets):
        if not self.all_valid(formsets):
            return False


        for formset in formsets:
            if 'QuizAnswer' in str(type(formset)):
                if not self.additional_answers_validate(formset):
                    return False
            if not formset.is_bound:
                pass
            for form in formset:
                # print('>>>form ', type(form))
                if hasattr(form, 'nested_formsets'):
                    if not self.all_valid_with_nesting(form.nested_formsets):
                        return False

                    # TODO - find out why this breaks when extra = 1 and just adding new item with no sub items
                    if (not hasattr(form, 'cleaned_data') or not form.cleaned_data) and \
                            self.formset_has_nested_data(form.nested_formsets):
                        form._errors["__all__"] = form.error_class(
                            [u"Напишите вопрос"]
                        )
                        return False
        return True

    @staticmethod
    def additional_answers_validate(formset):
        """ This method validate answers amount and correct answers amount"""

        question = formset.instance.question
        if not question:
            # in this case wokrs another validator
            return True

        answers = list(filter(lambda x: x , formset.cleaned_data))
        correct_answers_amount: int = len(list(filter(lambda x: x.get('is_correct'), answers)))
        answers_amount = len(answers)
        errors = []

        if correct_answers_amount == 0:
            errors.append('Хотя бы один варинант должен быть правильный')
        if correct_answers_amount == answers_amount:
            errors.append('Все варианты не могут быть правильными')
        if answers_amount < 2:
            errors.append('Должно быть хотя бы 2 варианта ответов')

        if errors:
            formset[0].errors["__all__"] = formset[0].error_class(errors)
            return False
        return True


# регистрирует модуль и его параметры
admin.site.register(Quiz, QuizAdmin)

# admin.site.register((Quiz,QuizAnswer,QuizQuestion))

# меняем заголовки в админке
admin.site.site_title = 'Управление тестами'
admin.site.site_header = 'Управление тестами'
