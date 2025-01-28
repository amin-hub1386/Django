from django.shortcuts import render
from rest_framework import viewsets

from doctors.models import DoctorUser
from doctors.serialize import DoctorSerializer


# Create your views here.

class DoctorViewSets(viewsets.ModelViewSet):
    queryset = DoctorUser.objects.all()
    serializer_class = DoctorSerializer
