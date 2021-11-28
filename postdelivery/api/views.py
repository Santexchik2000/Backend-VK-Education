from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_POST  # делаем views доступным только от этого метода
def create_contract(request):
    name = request.POST["name"]
    if len(name) >= 1:
        return JsonResponse({"message_status": f"Заказ {name} создан"})
    else:
        return JsonResponse({"message_status": "Введите имя заказа"},status=400)

@require_GET  # делаем views доступным только от этого метода
def get_list_contract(request):
    return JsonResponse({"message_status":"Получен список"})

@require_GET  # делаем views доступным только от этого метода
def get_info_contract(request, id):
    return JsonResponse({"message_status":f"Информация о заказе {id}"})