from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import serializers

@api_view(["POST"])
def register(request):
    serializer = serializers.RegistrationSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"success":"Registration successful"})

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)