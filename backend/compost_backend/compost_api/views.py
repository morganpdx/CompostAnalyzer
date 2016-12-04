from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
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
    API endpoint that allows CompostBins to be viewed or edited.
    POST requires: Device/Bin ID, sensor type, array of sensor data

    This approach assumes only one type of sensor per device.
    """
    queryset = CompostBin.objects.all()
    serializer_class = CompostBinSerializer

    @detail_route(methods=['post'])
    def add_sensor_data(self, request, pk=None):
        bin = self.get_object()
        sensor_type = request.data['sensor_type']
        sensor = CompostSensor.objects.get(type=sensor_type, bin=bin.id)
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():

            for d in serializer.data['values']:
                SensorData.objects.create(
                    sensor=sensor,
                    data=d
                )

            return Response({'status': 'new values saved'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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
