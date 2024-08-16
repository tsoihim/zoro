from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from .models import NetDevice
from .serializers import NetDeviceSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the devices index.")

class NetDeviceListCreate(generics.ListCreateAPIView):
    queryset = NetDevice.objects.all()
    serializer_class = NetDeviceSerializer
    
class NetDeviceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetDevice.objects.all()
    serializer_class = NetDeviceSerializer
