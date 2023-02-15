from django.db import models
from rest_framework import generics

from .models import User
from user.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

from rest_framework.decorators import api_view


class ListApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUserApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


@api_view(["POST"])
def LoginApiView(request, *argsm, ** kwargs):
    # "pbkdf2_sha256$390000$nOKT5wTdebHLwvyMdWCsX2$9lJP0nrCvmYYuxh/2LKLXKuXkwy6R5NX6Q57dxItUeQ="
    email = None
    password = None
    try:
        email = request.data['email']
        password = request.data['password']
    except:
        if email is None:
            return Response({'message': "Email required"})
        if password is None:
            return Response({'message': "Password required"})
    else:
        instance = {}
        try:
            instance = User.objects.get(
                email=email,
            )
        except Exception as e:
            print(e)
            return Response({'message': "Incorrect email or password"})
        data = {}
        if instance:
            data = UserSerializer(instance).data
            checkpassword = check_password(password, data['password'])
            print(checkpassword)
            if checkpassword:
                return Response(data)
            return Response({'message': "Incorrect email or password"})


class CreateUserApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
