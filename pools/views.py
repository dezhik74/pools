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


class CreateAnswer(APIView):

    def post(self, request, poll, usr, format=None):
        # {"answer_text": "еуые21"}
        print(request.data)
        print(poll)
        print(usr)
        # data = {"answer_text": "еуые21"}
        data = request.data
        try:
            new_poll = Poll.objects.get(pk=poll)
        except Poll.DoesNotExist:
            print('Неправильный полл')
            return Response('poll does not exist', status=status.HTTP_400_BAD_REQUEST)
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save(poll, usr)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateAnswer(generics.CreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer

    # def perform_create(self, serializer):
    #     print(f'тут poll {self.kwargs["poll"]} id {self.kwargs["id"]}')
    #     try:
    #         person = Person.objects.get(pk=self.kwargs["id"])
    #     except Person.DoesNotExist:
    #         person = Person(person_name=str(self.kwargs["id"]))
    #         person.save()
    #     try:
    #         poll = Poll.objects.get(pk=self.kwargs["poll"])
    #     except Poll.DoesNotExist:
    #         print('Неправильный полл')
    #         print(Response(status=status.HTTP_400_BAD_REQUEST))
    #         return Response(status=status.HTTP_400_BAD_REQUEST, exception=True)
    #     if serializer.is_valid():
    #         # print ("правильно", serializer.data)
    #         # print(person)
    #         # print(poll)
    #         a = Answer(answer_text=serializer.data['answer_text'])
    #         a.poll = poll
    #         a.usr = person
    #         a.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)





