from django.urls import path
from ui import views 

urlpatterns = [
    path('', views.main),
]