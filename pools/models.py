from django.db import models
from django.contrib.auth.models import User


class Poll (models.Model):

    name = models.CharField(max_length=250, verbose_name='Название опроса')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начала опроса')
    end_date = models.DateField(verbose_name='Дата конца опроса')

    def __str__(self):
        return f'Опрос номер {self.pk} название {self.name} период [{str(self.start_date)} - {str(self.end_date)}]'


class Question (models.Model):
    ANSW_TEXT = 'text'
    ANSW_1_VAR = 'one'
    ANSW_MANY_VAR = 'many'

    QUEST_CHOICE = [
        (ANSW_TEXT, 'Текст'),
        (ANSW_1_VAR, 'Один вариант'),
        (ANSW_MANY_VAR, 'Несколько вариантов'),
    ]

    question_text = models.CharField(max_length=500, verbose_name='Текст вопроса')
    attribute = models.CharField(max_length=4, choices=QUEST_CHOICE, default=ANSW_TEXT, verbose_name='Аттрибут')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name='Опрос', related_name='questions')

    def __str__(self):
        return f'Вопрос номер {self.pk} Текст вопроса {self.question_text} тип  {self.attribute} опрос {self.poll.pk}'


class QVariant (models.Model):
    q_variant_text = models.CharField(max_length=500, verbose_name='Вариант ответа')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='q_variants')

    def __str__(self):
        return f'Текст варианта ответа {self.q_variant_text}'


class Person (models.Model):
    person_name = models.CharField(max_length=30, verbose_name='Ник пользователя', default='Kuku')

    def __str__(self):
        return f'Персона id={self.pk} имя={self.person_name}'


class PollResult (models.Model):
    usr = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='poll_results', verbose_name='Автор ответа')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name='Опрос')
    poll_result_name = models.CharField(max_length=250, verbose_name='Название опроса')

    def __str__(self):
        return f'Резльтаты опроса. Персона {self.usr}. Опрос {self.poll_result_name}'


class PollResultQuestion (models.Model):
    question_text = models.CharField(max_length=500, verbose_name='Текст вопроса')
    poll_result = models.ForeignKey('PollResult', on_delete=models.CASCADE, verbose_name='Результаты опроса',
                                    related_name='poll_result_questions')

    def __str__(self):
        return f'Вопрос-> {self.question_text}'


class Answer (models.Model):
    poll_result_question = models.ForeignKey('PollResultQuestion', on_delete=models.CASCADE,
                                             related_name='answers', verbose_name='Ответ')
    answer_text = models.CharField(max_length=500, verbose_name='Текст варианта ответа')

    def __str__(self):
        return f'Текст ответа {self.answer_text}'
