#from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
#from django_filters.rest_framework import DjangoFilterBackend

# i created views to handle API endpoints

# create food and display
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


# retrieve, update or delete Food by id
class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

   
   