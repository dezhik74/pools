import pprint

from django.db.models import Model
from rest_framework import serializers

from .models import Poll, QVariant, Person, Question, PollResult, PollResultQuestion, Answer


class PollListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date')


class QVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QVariant
        fields = ('q_variant_text',)


class QuestionDetailSerializer (serializers.ModelSerializer):

    q_variants = QVariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question_text', 'attribute', 'q_variants')


class PollDetailSerializer(serializers.ModelSerializer):

    questions = QuestionDetailSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date', 'questions')


class AnswerSerializer (serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['answer_text']


class PollResultQuestionSerializer (serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = PollResultQuestion
        fields = ['id', 'question_text', 'answers']


class PollResultSerializer(serializers.ModelSerializer):
    poll_result_questions = PollResultQuestionSerializer(many=True)

    class Meta:
        model = PollResult
        fields = ['id', 'poll_result_name', 'poll', 'poll_result_questions']


class PollResultCreateSerializer(serializers.ModelSerializer):

    poll_result_questions = PollResultQuestionSerializer(many=True)

    # person = serializers.IntegerField()

    class Meta:
        model = PollResult
        fields = ['id', 'poll_result_name', 'poll', 'usr', 'poll_result_questions']

    def save(self):
        validated_data = self.validated_data
        poll_result = PollResult.objects.create(poll=validated_data['poll'],
                                                poll_result_name=validated_data['poll_result_name'],
                                                usr=validated_data['usr'])
        for poll_result_question in validated_data['poll_result_questions']:
            q = PollResultQuestion.objects.create(question_text=poll_result_question['question_text'],
                                                  poll_result=poll_result)
            for answer in poll_result_question['answers']:
                a = Answer.objects.create(answer_text=answer['answer_text'],
                                          poll_result_question=q)
            q.save()
        poll_result.save()


class PersonDetailSerializer(serializers.ModelSerializer):
    poll_results = PollResultSerializer(many=True)

    class Meta:
        model = Person
        fields = ['id', 'person_name', 'poll_results']



# class AnswerCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ('pool', 'usr')
#
#

# СТАРЫЙ КОД!!!!!






# class AnswerSerializer(serializers.ModelSerializer):
#
#     # usr = PersonDetailSerializer(many=False)
#     # poll = PollSerializer(many=False)
#
#     class Meta:
#         model = Answer
#         fields = ['answer_text']
#         # depth = 1
#
#     def save(self, poll, usr):
#         new_poll = Poll.objects.get(pk=poll)
#         try:
#             person = Person.objects.get(pk=usr)
#         except Person.DoesNotExist:
#             person = Person(person_name=str(self.kwargs["id"]))
#             person.save()
#         print(self.validated_data['answer_text'])
#         a = Answer(answer_text=self.validated_data['answer_text'])
#         a.poll = new_poll
#         a.usr = person
#         a.save()
#
#
#     def create(self, validated_data):
#         print('Новый объект')
#         print(validated_data)
#         return Answer(validated_data)
#
#
#

