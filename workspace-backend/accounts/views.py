from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny 
from .serializers import MeSerializer, RegisterSerializer
# My view 
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response(MeSerializer(request.user).data)




class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
