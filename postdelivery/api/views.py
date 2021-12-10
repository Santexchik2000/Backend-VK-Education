from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

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