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

    def __str__(self):
        return f'number {self.pk} {self.name} -> [[[{str(self.start_date)} - {str(self.end_date)}]]]'


class Variant (models.Model):
    variant = models.CharField(max_length=500, verbose_name='Вариант ответа')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='variants')

    def __str__(self):
        return self.variant


class Person (models.Model):
    person_name = models.CharField(max_length=30, verbose_name='Ник пользователя', default='Kuku')

    def __str__(self):
        return f'id={self.pk} мия={self.person_name}'


class Answer (models.Model):
    usr = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='answers')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='poll')
    answer_text = models.CharField(max_length=500, verbose_name='Ответ')

    def __str__(self):
        return f'юзер {self.usr} опрос {self.poll} ответ {self.answer_text}'



