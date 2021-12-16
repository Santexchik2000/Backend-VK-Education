from django.urls import path
from api import views

from db import models

urlpatterns = [
    path('user/create/', views.create_user),
    path('user/<int:id>/', views.user_info),
    path('user/all/', views.user_list),
    path('user/<int:id>/edit/', views.edit_user),
    path('user/<int:id>/delete/', views.user_delete),
    path('adresssender/create/',views.create_adres_sender,{"Model":models.AdressSender}),
    path('adressrecipient/create/',views.create_adres_recipient,{"Model":models.AdressRecipient}),
    path('adresssender/<int:id>/',views.adress_info,{"Model":models.AdressSender}),
    path('adressrecipient/<int:id>/',views.adress_info,{"Model":models.AdressRecipient}),
    path('adresssender/all/', views.adress_list, {"Model": models.AdressSender}),
    path('adressrecipient/all/', views.adress_list, {"Model": models.AdressRecipient}),
    path('adresssender/<int:id>/edit/', views.edit_adress, {"Model": models.AdressSender}),
    path('adressrecipient/<int:id>/edit/', views.edit_adress, {"Model": models.AdressRecipient}),
    path('adresssender/<int:id>/delete/', views.adress_delete, {"Model": models.AdressSender}),
    path('adressrecipient/<int:id>/delete/', views.adress_delete, {"Model": models.AdressRecipient}),


]
