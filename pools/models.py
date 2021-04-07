from django.db import models
from django.contrib.auth.models import User

class Poll (models.Model):

    ANSW_TEXT = 'text'
    ANSW_1_VAR = 'one'
    ANSW_MANY_VAR = 'many'

    QUEST_CHOICE = [
        (ANSW_TEXT, 'Текст'),
        (ANSW_1_VAR, 'Один вариант'),
        (ANSW_MANY_VAR, 'Несколько вариантов'),
    ]

    name = models.CharField(max_length=250, verbose_name='Название опроса')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начала опроса')
    end_date = models.DateField(verbose_name='Дата конца опроса')
    question_text = models.CharField(max_length=500, verbose_name='Сам вопрос')
    attribute = models.CharField(max_length=4, choices=QUEST_CHOICE, default=ANSW_TEXT)


class Variant (models.Model):
    variant = models.CharField(max_length=500, verbose_name='Вариант ответа')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='variants')


class Person (User):

    # person_id = models.IntegerField(unique=True)

    class Meta:
        proxy = True


class Answer (models.Model):
    usr = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='answers')
    poll = models.OneToOneField('Poll', on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=500, verbose_name='Ответ')


