import json
from typing import Dict
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from api.decorators import require_body
from db.models import Client

@csrf_exempt
@require_POST
@require_body('POST', ['lname', 'fname', 'login', 'email', 'telefon'])
def create_user(request, Model):
    info = json.loads(request.body)
    # {"lname":"name"}
    user = Model.objects.create(**info)
    return JsonResponse({"status":"Создан новый объект"})  
    # return Client.objects.create(lname="name",...)

@require_GET
def user_info(request, id, Model):
    try:
        info = Model.objects.get(id=id)
        return JsonResponse({"fname":info.fname,"lname": info.lname,"login": info.login,"email": info.email,"telefon": info.telefon})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Пользователь c {id} не найден"}, status=400)
    
@require_GET
def user_list(request, Model):
    user_list = Model.objects.all()
    return JsonResponse(list(user_list.values()), safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
@require_body('PUT', ['lname', 'fname', 'login', 'email', 'telefon'])
def edit_user(request, id, Model):
    data = json.loads(request.body)
    try:
        info = Model.objects.get(id=id)
        info.lname = data['lname']
        info.fname = data['fname']
        info.login = data['login']
        info.email = data['email']
        info.telefon = data['telefon']
        info.save()
        return JsonResponse({"Объект":"Изменён","Пользователь":{"fname":info.fname,"lname": info.lname,"login": info.login,"email": info.email,"telefon": info.telefon}})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Пользователь c {id} не найден"}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def user_delete(request, id, Model):
    try:
        info = Model.objects.get(id=id)
        info.delete()
        return JsonResponse({"Пользователь":"Удалён"})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Пользователь c {id} не найден"}, status=400)


@csrf_exempt
@require_POST
@require_body('POST', ['city', 'street', 'house', 'flat'])
def create_adres_sender(request, Model):
    info = json.loads(request.body)
    # {"city":"city"}
    adres_sender = Model.objects.create(**info)
    return JsonResponse({"status":"Создан новый объект"})  
    # return Client.objects.create(city="city",...)

@csrf_exempt
@require_POST
@require_body('POST', ['city', 'street', 'house', 'flat'])
def create_adres_recipient(request, Model):
    info = json.loads(request.body)
    # {"city":"city"}
    adres_recipient = Model.objects.create(**info)
    return JsonResponse({"status":"Создан новый объект"})  
    # return Client.objects.create(city="city",...)

@require_GET
def adress_info(request, id, Model):
    try:
        info = Model.objects.get(id=id)
        return JsonResponse({"city":info.city,"street": info.street,"house": info.house,"flat": info.flat})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Адрес c id {id} не найден"}, status=400)
    
@require_GET
def adress_list(request, Model):
    adress_list = Model.objects.all()
    return JsonResponse(list(adress_list.values()), safe=False)



@csrf_exempt
@require_http_methods(["PUT"])
@require_body('PUT', ['city', 'street', 'house', 'flat'])
def edit_adress(request, id, Model):
    data = json.loads(request.body)
    try:
        info = Model.objects.get(id=id)
        info.city = data['city']
        info.street = data['street']
        info.house = data['house']
        info.flat = data['flat']
        info.save()
        return JsonResponse({"Объект":"Изменён","Адрес":{"city":info.city,"street": info.street,"house": info.house,"flat": info.flat}})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Адрес c id {id} не найден"}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def adress_delete(request, id, Model):
    try:
        info = Model.objects.get(id=id)
        info.delete()
        return JsonResponse({"Адрес":"Удалён"})
    except Model.DoesNotExist:
        return JsonResponse({"error":f"Адрес c id{id} не найден"}, status=400)
