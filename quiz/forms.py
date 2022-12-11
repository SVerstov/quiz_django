from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from .models import Quiz, QuizAnswer, QuizQuestion


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'short_description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer
        fields = '__all__'
        widgets = {
            'size': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


AnswerFormSet = inlineformset_factory(
    QuestionForm, QuizAnswer, form=QuizAnswerForm,
    extra=1, can_delete=True, can_delete_extra=True
)
