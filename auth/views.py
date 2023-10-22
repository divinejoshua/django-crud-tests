from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404,redirect
import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from . import serializers
from .models import Account,SocialLogin,UserOtp

#For authentication
from django.contrib.auth import authenticate,logout

#For gmail login
from django.contrib.auth.decorators import login_required

#For email verification
from rest_framework.decorators import api_view, permission_classes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail


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