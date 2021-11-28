from django.urls import path
from api import views 

urlpatterns = [
    path('contracts/', views.get_list_contract),
    path('contracts/<int:id>/', views.get_info_contract),
    path('contracts/create/', views.create_contract),
]