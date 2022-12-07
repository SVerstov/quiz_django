from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from .models import Quiz, QuizAnswer, QuizQuestion

#
# # QuizFormSet = inlineformset_factory(Quiz, QuizQuestion, extra=1)
# # QuestionFormset = inlineformset_factory(QuizQuestion, QuizAnswer, extra=1)
#
# class BaseChildrenFormset(BaseInlineFormSet):
#     pass
#
#
# ChildrenFormset = inlineformset_factory(Quiz,
#                                         QuizQuestion,
#                                         formset=BaseChildrenFormset,
#                                         extra=1)
#
#
# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = QuizQuestion
#         fields = ('quiz', 'question')
#
#
class TestForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('quiz', 'question')
        # fields = ('title', 'text',)
