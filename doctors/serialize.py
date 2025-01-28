from rest_framework.serializers import ModelSerializer

from doctors.models import DoctorUser


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = DoctorUser
        fields = '__all__'
