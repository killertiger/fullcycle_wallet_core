from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets

from core.models import Account
from core.serializers import AccountSerializer

# Create your views here.
def balances(request):
    return HttpResponse('Hello, World!')

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer