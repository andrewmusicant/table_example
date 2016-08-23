from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from table_app.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render, HttpResponse


def index(self):
    return HttpResponse('Hello world')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
