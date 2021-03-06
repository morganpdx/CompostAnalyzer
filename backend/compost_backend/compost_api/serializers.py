from django.contrib.auth.models import User, Group
from rest_framework import serializers
from compost_backend.compost_user.models import CompostUser
from compost_backend.compost_bin.models import CompostBin
from compost_backend.compost_sensor.models import CompostSensor
from compost_backend.sensor_data.models import SensorData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CompostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompostUser
        fields = ('id', 'first_name', 'last_name')


class CompostBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompostBin
        fields = ('id', 'name', 'description', 'user')


class CompostSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompostSensor
        fields = ('id', 'type', 'bin')


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'timestamp', 'value', 'sensor')