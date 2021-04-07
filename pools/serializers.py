from rest_framework import serializers

from .models import Poll, Variant, Person, Answer


class PollSerializer (serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'name', 'start_date', 'end_date', 'question_text', 'attribute', 'variants')
        depth = 1


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    # the_poll = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # the_poll = PollSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = ['answer_text', 'poll']
        depth = 1


class PersonDetailSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['id', 'answers']


