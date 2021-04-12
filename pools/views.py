from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Poll, QVariant, Person, Answer, PollResult
from .serializers import PollListSerializer, PollDetailSerializer, PersonDetailSerializer, PollResultSerializer, \
    PollResultCreateSerializer
import datetime
from rest_framework.response import Response



class PollsList (generics.ListAPIView):
    """Вывод всех опросов"""
    queryset = Poll.objects.all()
    serializer_class = PollListSerializer


class ActivePolls(generics.ListAPIView):
    """Вывод только активных опросов"""
    queryset = Poll.objects.filter(end_date__gte=datetime.date.today())
    serializer_class = PollListSerializer


class PollDetailView(generics.RetrieveAPIView):
    """Вывод одного опроса со списком вопросов и вариантов"""
    queryset = Poll.objects.all()
    serializer_class = PollDetailSerializer


class PersonView (generics.RetrieveAPIView):
    """Вывод результатов всех опросов (с ответами), в которых участвовал юзер"""
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer


class CreatePollResultView(APIView):
    """Создание результатов опроса. Если id пользователя нет, то создается новый пользователь"""

    def post(self, request, format=None):
        data = request.data
        usr_pk = data['usr']
        try:
            Person.objects.get(pk=usr_pk)
        except Person.DoesNotExist:
            Person.objects.create(pk=usr_pk, person_name=f'Generated {usr_pk}')
        serializer = PollResultCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





