from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404,redirect
import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from . import serializers
#For authentication

# Create your views here.
class user_view(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {}
        user =  get_object_or_404(Account, email=request.user.email)
        serializer = serializers.AccountSerializer(user)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

     #for Updating user 
    def put(self, request):
        data = {}
        user =  get_object_or_404(Account, email=request.user.email)
        serializer = serializers.AccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
        else:
            data = serializer.errors   
        return Response(data,  status=status.HTTP_200_OK)

#Register users
class register_view(APIView):
    def post(self, request):
        data = {} 
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)