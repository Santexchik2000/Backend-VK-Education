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
from user.decorators import login_required
from rest_framework import viewsets
from api.serializers import RecipientSerializer,AdressSenderSerializer,AdressRecipientSerializer,RouteSerializer,UserProfileSerializer,ContractSerializer
from db.models import Contract, Recipient, AdressSender, AdressRecipient, Route
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

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
    queryset = User.objects.all() 


    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True).data)

    @login_required
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        return Response(self.serializer_class(user).data)

    @login_required
    @action(detail=False)
    def me(self, request):
        return Response(self.serializer_class(request.user).data)


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

