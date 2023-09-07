from django.shortcuts import render

def index(request):
    return render(request, 'food/templates/food/food.html')

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
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name', 'calories']

# retrieve, update or delete Food by id
class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

   
   
   
   
   
   
   
    #get all the drinks, serialize them and return json

#def Food_list(request):
   # Food = Food.objects.all()
    #serializer = FoodSerializer(Food, many=True)
   # return JsonResponse(serializer.data)