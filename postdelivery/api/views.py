import json
from typing import Dict
from django.contrib.auth import get_user
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from api.decorators import require_body
from user.models import UserProfile as User
from rest_framework import viewsets
from api.serializers import RecipientSerializer,AdressSenderSerializer,AdressRecipientSerializer,RouteSerializer,UserProfileSerializer,ContractSerializer
from db.models import Contract, Recipient, AdressSender, AdressRecipient, Route

class RecipientViewSet(viewsets.ModelViewSet):
    serializer_class = RecipientSerializer
    queryset = Recipient.objects.all()

class AdressSenderViewSet(viewsets.ModelViewSet):
    serializer_class = AdressSenderSerializer
    queryset = AdressSender.objects.all()

class AdressRecipientViewSet(viewsets.ModelViewSet):
    serializer_class = AdressRecipientSerializer
    queryset = AdressRecipient.objects.all()

class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all() #?

class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
