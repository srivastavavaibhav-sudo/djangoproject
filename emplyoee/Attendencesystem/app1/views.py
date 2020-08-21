from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models .members import Members
from .models .activity_periods import Activity_periods 
from .  serializers import mySerializer,mytimeSerializer
from rest_framework import viewsets



# <<-------view for members of attendence records------->>
class SystemAPI(viewsets.ModelViewSet):
    serializer_class = mySerializer
    queryset = Members.objects.all()[:5]


# <<-------view for time  records------->>
class TimeAPI(viewsets.ModelViewSet):
    serializer_class = mytimeSerializer
    queryset = Activity_periods.objects.all()[:5]