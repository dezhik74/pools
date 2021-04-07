from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Poll, Variant, Person, Answer
from .serializers import PollSerializer, PersonDetailSerializer, AnswerSerializer
import datetime
from rest_framework.response import Response


class PollList (generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ActivePolls(generics.ListAPIView):
    queryset = Poll.objects.filter(end_date__gte=datetime.date.today())
    serializer_class = PollSerializer


class PersonView (generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer


class PollView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class CreateAnswer(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        print(f'тут poll {self.kwargs["poll"]} id {self.kwargs["id"]}')
        try:
            person = Person.objects.get(pk=self.kwargs["id"])
        except:
            person = Person(person_name=str(self.kwargs["id"]))
            person.save()
        try:
            poll = Poll.objects.get(pk=self.kwargs["poll"])
        except:
            print('Неправильный полл')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            # print ("правильно", serializer.data)
            # print(person)
            # print(poll)
            a = Answer(answer_text=serializer.data['answer_text'])
            a.poll = poll
            a.usr = person
            a.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)





