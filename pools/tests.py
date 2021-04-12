from django.test import TestCase
from .models import Poll, Question, QVariant
from datetime import date, timedelta
import json
from rest_framework.test import APIClient
import pprint



# Create your tests here.

class PollAPITestCase (TestCase):

    def setUp(self) -> None:
        p1 = Poll.objects.create(name="Опрос 1", end_date=date.today() + timedelta(days=10))
        q1 = Question.objects.create(question_text='Опрос 1 Вопрос 1', attribute='text', poll=p1)
        q2 = Question.objects.create(question_text='Опрос 1 Вопрос 2', attribute='one', poll=p1)
        q3 = Question.objects.create(question_text='Опрос 1 Вопрос 3', attribute='many', poll=p1)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 2 Вар 1', question=q2)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 2 Вар 2', question=q2)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 2 Вар 3', question=q2)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 3 Вар 1', question=q3)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 3 Вар 2', question=q3)
        QVariant.objects.create(q_variant_text='Опрос 1 Вопрос 3 Вар 3', question=q3)

        p2 = Poll.objects.create(name="Опрос 2", end_date=date.today() + timedelta(days=10))
        q21 = Question.objects.create(question_text='Опрос 2 Вопрос 1', attribute='text', poll=p2)
        q22 = Question.objects.create(question_text='Опрос 2 Вопрос 2', attribute='one', poll=p2)
        q23 = Question.objects.create(question_text='Опрос 2 Вопрос 3', attribute='many', poll=p2)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 2 Вар 1', question=q22)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 2 Вар 2', question=q22)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 2 Вар 3', question=q22)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 3 Вар 1', question=q23)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 3 Вар 2', question=q23)
        QVariant.objects.create(q_variant_text='Опрос 2 Вопрос 3 Вар 3', question=q23)

        p3 = Poll.objects.create(name="Опрос 3 - окончен", end_date=date.today() - timedelta(days=10))
        q31 = Question.objects.create(question_text='Опрос 3 Вопрос 1', attribute='text', poll=p3)

        self.c = APIClient()

    def test_polls(self):
        print('---------------- Все опросы')
        j = json.loads(self.c.get('/polls').content)
        pprint.pprint(j, sort_dicts=False)

        print('\n---------------- Активные опросы')
        j = json.loads(self.c.get('/active-polls').content)
        pprint.pprint(j, sort_dicts=False)

        print('\n---------------- Вывод детализации опроса poll/<pk>')
        for i in range (1,4):
            print(f'-------------- Опрос №{i}')
            j = json.loads(self.c.get(f'/poll/{i}').content)
            pprint.pprint(j, sort_dicts=False)

    def test_create_poll_results(self):
        print('--------------- Делаем новый результат опроса от старого пользователя')
        data ={'poll_result_name': 'Опрос 1',
             'poll': 1,
             'usr': 2,
             'poll_result_questions': [{'question_text': 'Опрос 1 Вопрос 1',
                                        'answers': [{'answer_text': 'произвольный ответ'}]},
                                       {'question_text': 'Опрос 1 Вопрос 2',
                                        'answers': [{'answer_text': 'О1 В2 Вар 3'}]},
                                       {'question_text': 'Опрос 1 Вопрос 3',
                                        'answers': [{'answer_text': 'О1 В3 Вар 1'},
                                                    {'answer_text': 'О1 В3 Вар 3'}]}]}
        self.c.post('/create-poll-result', data, format='json')
        print('--------------Делаем запрос результатов опросов по новому юзеру')
        j = json.loads(self.c.get('/person/2').content)
        print(j)