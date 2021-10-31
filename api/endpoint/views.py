# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from api.models import results
from .serializers import ResultDataSerializer

from api.models import states
from .serializers import StateDataSerializer
class ResultsDataApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        params = request.query_params
        if(len(params) == 0):
            result = results.objects.all()
        elif("statename" in params.keys()):
            result = results.objects.filter(statename = params['statename'])
        serializer = ResultDataSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StatesApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        params = request.query_params
        if(len(params) == 0):
            statesVar = states.objects.all()
        elif("stateabrv" in params.keys()):
            statesVar = states.objects.filter(stateabrv = params['stateabrv'])

        serializer = StateDataSerializer(statesVar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

