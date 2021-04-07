from django.shortcuts import render
from rest_framework import generics
from .models import Poll, Variant
from .serializers import PollSerializer
import datetime


class PollList (generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ActivePolls(generics.ListAPIView):
    queryset = Poll.objects.filter(end_date__gte=datetime.date.today())
    serializer_class = PollSerializer

