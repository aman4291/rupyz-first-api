# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from staff_api.models import Staff
from staff_api.serializers import PublicListSerializer

# Create your views here.


class StaffData(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = PublicListSerializer
