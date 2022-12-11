from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from .models import Quiz, QuizAnswer, QuizQuestion





class TestForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('quiz', 'question')
        # fields = ('title', 'text',)
