# api/api/serializers.py
from rest_framework import serializers
from api.models import results
from api.models import states


class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = states
        fields = ["statename", "stateabrv"]


class ResultDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = results
        fields = ["statename", "result", "demvotes", "repvotes", "othervotes", "dempercent", "reppercent", "otherpercent", "stateid"]
