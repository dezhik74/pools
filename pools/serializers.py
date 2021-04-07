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


class PersonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'answers']
        depth = 2


class AnswerSerializer(serializers.ModelSerializer):

    # usr = PersonDetailSerializer(many=False)
    # poll = PollSerializer(many=False)

    class Meta:
        model = Answer
        fields = ['answer_text']
        # depth = 1

    def save(self, poll, usr):
        new_poll = Poll.objects.get(pk=poll)
        try:
            person = Person.objects.get(pk=usr)
        except Person.DoesNotExist:
            person = Person(person_name=str(self.kwargs["id"]))
            person.save()
        print(self.validated_data['answer_text'])
        a = Answer(answer_text=self.validated_data['answer_text'])
        a.poll = new_poll
        a.usr = person
        a.save()


    def create(self, validated_data):
        print('Новый объект')
        print(validated_data)
        return Answer(validated_data)




