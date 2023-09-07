from rest_framework import serializers
from .models import Food


#create serializers to convert model instances to json


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        #fields = ['id', name', 'image', 'description', 'calories', 'carbohydrates', 'proteins', 'fats']