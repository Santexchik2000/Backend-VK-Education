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
# @require_POST  # делаем views доступным только от этого метода
def create_contract(request):
    if request.method == "POST":
        name = request.POST["name"]
        if len(name) >= 1:
            return JsonResponse({"message_status": f"Заказ {name} создан"})
        else:
            return JsonResponse({"message_status": "Введите имя заказа"},status=400)
    else: 
        return HttpResponseNotAllowed(['POST'])

# @require_GET  # делаем views доступным только от этого метода
def get_list_contract(request):
    if request.method == "GET": 
        return JsonResponse({"message_status":"Получен список"})
    else:
        return HttpResponseNotAllowed(['GET'])

# @require_GET  # делаем views доступным только от этого метода
def get_info_contract(request, id):
    if request.method == "GET": 
        return JsonResponse({"message_status":f"Информация о заказе {id}"})
    else:
        return HttpResponseNotAllowed(['GET'])
    
###

@csrf_exempt
@require_POST
@require_body('POST', ['lname', 'fname', 'login', 'email', 'telefon'])
def create_user(request, Model):
    info = json.loads(request.body)
    # {"lname":"Amir"}
    user = Model.objects.create(**info)
    return JsonResponse({"status":"Создан новый объект"})  
    # return Client.objects.create(lname="Amir",...)

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
