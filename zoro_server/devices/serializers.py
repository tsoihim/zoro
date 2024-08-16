from rest_framework import serializers
from .models import NetDevice 

class NetDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetDevice 
        fields = '__all__'
