from django.urls import path

from .views import NetDeviceListCreate, NetDeviceRetrieveUpdateDestroy 

urlpatterns = [
    path('', 
        NetDeviceListCreate.as_view(), name="net-device-list"),
    path('<int:pk>/', 
        NetDeviceRetrieveUpdateDestroy.as_view(), name="net-device-detail"),
]
