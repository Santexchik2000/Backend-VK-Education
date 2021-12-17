from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView

router = DefaultRouter()
router.register(r'recipient',views.RecipientViewSet, basename='recipient')
router.register(r'adress_sender',views.AdressSenderViewSet, basename='adress_sender')
router.register(r'adress_recipient',views.AdressRecipientViewSet,basename='adress_recipient')
router.register(r'route',views.RouteViewSet,basename='route')
router.register(r'user_profile',views.UserProfileViewSet,basename='user_profile')
router.register(r'contract',views.ContractViewSet,basename='contract')


urlpatterns = [
   path('', include(router.urls)),

   path('schema/', SpectacularAPIView.as_view(), name='schema'),
   
   path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
   path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
