# -*- coding:UTF-8 -*-
from rest_framework import serializers

from models import Agent


class AgentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ('id', 'name', 'zipcode')
