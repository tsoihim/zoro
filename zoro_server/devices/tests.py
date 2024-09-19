from django.db import IntegrityError
from django.test import TestCase
from devices.models import NetDevice

class NetDeviceTestCase(TestCase):
    def setUp(self):
        NetDevice.objects.create(serial="A123", ip="12.1.1.1")
        NetDevice.objects.create(serial="A124", ip="12.1.1.1")

    def insert_dup(self):
        NetDevice.objects.create(serial="A124", ip="12.1.1.1")

    def test_net_device_dump(self):
        print(NetDevice.objects.all().values())
        self.assertRaises(IntegrityError, self.insert_dup)
