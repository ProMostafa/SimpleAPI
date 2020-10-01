from django.shortcuts import render
from .models import Account  ,ClintOrder
from .serializer import AccountSerializer , ClientOrderSerializer
from rest_framework import viewsets

# Create your views here.

class UsersAccounts(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer



class ClientsOrder(viewsets.ModelViewSet):
    queryset=ClintOrder.objects.all()
    serializer_class=ClientOrderSerializer
