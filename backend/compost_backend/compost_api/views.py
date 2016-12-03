from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from compost_backend.compost_user.models import CompostUser
from compost_backend.compost_bin.models import CompostBin
from compost_backend.compost_sensor.models import CompostSensor
from compost_backend.sensor_data.models import SensorData
from compost_backend.compost_api.serializers import UserSerializer, GroupSerializer, CompostUserSerializer, CompostBinSerializer, CompostSensorSerializer, SensorDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CompostUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CompostUsers to be viewed or edited.
    """
    queryset = CompostUser.objects.all()
    serializer_class = CompostUserSerializer


class CompostBinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CospostBins to be viewed or edited.
    """
    queryset = CompostBin.objects.all()
    serializer_class = CompostBinSerializer


class CompostSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CompostSensors to be viewed or edited.
    """
    queryset = CompostSensor.objects.all()
    serializer_class = CompostSensorSerializer


class SensorDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SensorData to be viewed or edited.
    """
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer



