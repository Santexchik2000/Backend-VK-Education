from django.urls import path
from api import views

from db import models

urlpatterns = [
    path('client/create/', views.create_user, {"Model": models.Client}),
    path('manager/create/', views.create_user, {"Model": models.Manager}),
    path('loader/create/', views.create_user, {"Model": models.Loader}),
    path('driver/create/', views.create_user, {"Model": models.Driver}),
    path('client/<int:id>/', views.user_info, {"Model": models.Client}),
    path('manager/<int:id>/', views.user_info, {"Model": models.Manager}),
    path('loader/<int:id>/', views.user_info, {"Model": models.Loader}),
    path('driver/<int:id>/', views.user_info, {"Model": models.Driver}),
    path('client/all/', views.user_list, {"Model": models.Client}),
    path('manager/all/', views.user_list, {"Model": models.Manager}),
    path('loader/all/', views.user_list, {"Model": models.Loader}),
    path('driver/all/', views.user_list, {"Model": models.Driver}),
    path('client/<int:id>/edit/', views.edit_user, {"Model": models.Client}),
    path('manager/<int:id>/edit/', views.edit_user, {"Model": models.Manager}),
    path('loader/<int:id>/edit/', views.edit_user, {"Model": models.Loader}),
    path('driver/<int:id>/edit/', views.edit_user, {"Model": models.Driver}),
    path('client/<int:id>/delete/', views.user_delete, {"Model": models.Client}),
    path('manager/<int:id>/delete/', views.user_delete, {"Model": models.Manager}),
    path('loader/<int:id>/delete/', views.user_delete, {"Model": models.Loader}),
    path('driver/<int:id>/delete/', views.user_delete, {"Model": models.Driver}),
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
