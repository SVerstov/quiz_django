# Generated by Django 4.1.3 on 2022-12-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_quizanswer_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswers',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='useranswers',
            name='user_answer',
        ),
        migrations.AddField(
            model_name='useranswers',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]