from rest_framework import serializers

from .models import Poll, Variant

class PollSerializer (serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


