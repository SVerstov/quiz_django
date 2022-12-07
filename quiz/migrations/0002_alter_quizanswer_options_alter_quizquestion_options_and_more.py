# Generated by Django 4.1.3 on 2022-12-04 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizanswer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pass_score',
            field=models.PositiveIntegerField(default=60, help_text='Минимальный результат (в процентах) для прохождения теста', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='quizanswer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Отметьте правильные'),
        ),
        migrations.AlterField(
            model_name='quizanswer',
            name='text',
            field=models.CharField(max_length=250, verbose_name='Варианты ответа'),
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='question',
            field=models.CharField(max_length=1000, verbose_name='Вопрос'),
        ),
    ]