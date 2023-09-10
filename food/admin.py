from django.contrib import admin
from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'carbohydrates', 'proteins', 'fats')
    list_filter = ('name', 'calories')
    search_fields = ('name',)

# Register the admin classes for the models, 
admin.site.register(Food, FoodAdmin)