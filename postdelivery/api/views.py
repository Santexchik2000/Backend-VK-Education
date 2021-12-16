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

@csrf_exempt
@require_POST
@require_body('POST', ['last_name', 'first_name', 'login', 'email', 'telefon', 'role'])
def create_user(request):
    info = json.loads(request.body)
    User.objects.create(**info)

    # {"lname":"name"}
    return JsonResponse({"status":"Создан новый объект"})

@require_GET
def user_info(request, id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse({
            "fname":user.fname, 
            "lname": user.lname, 
            "login": user.login, 
            "email": user.email, 
            "telefon": user.telefon,
            "role": user.role,
            })
    except User.DoesNotExist:
        return JsonResponse({"error":f"Пользователь c {id} не найден"}, status=400)
    
@require_GET
def user_list(request):
    user_list = User.objects.all()
    return JsonResponse(list(user_list.values()), safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
@require_body('PUT', ['lname', 'fname', 'login', 'email', 'telefon', 'role'])
def edit_user(request, id):
    data = json.loads(request.body)
    try:
        user = User.objects.get(id=id)
        user.lname = data['lname']
        user.fname = data['fname']
        user.login = data['login']
        user.email = data['email']
        user.telefon = data['telefon']
        user.role = data['role']
        user.save()
        return JsonResponse({
            "Объект":"Изменён",
            "Пользователь": { 
                "fname":user.fname, 
                "lname": user.lname, 
                "login": user.login, 
                "email": user.email, 
                "telefon": user.telefon,
                "role": user.role, 
                }})
    except User.DoesNotExist:
        return JsonResponse({"error":f"Пользователь c {id} не найден"}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def user_delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse({"Пользователь":"Удалён"})
    except User.DoesNotExist:
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
