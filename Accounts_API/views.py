from django.shortcuts import render
from .models import Account 
from .serializer import AccountSerializer
from rest_framework import viewsets

# Create your views here.

class UsersAccounts(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
