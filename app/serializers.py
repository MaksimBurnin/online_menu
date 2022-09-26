from rest_framework import serializers
from .models import Category, Allergen, Dish

class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'position']

class DishSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    allergens = serializers.PrimaryKeyRelatedField(many=True, queryset=Allergen.objects.all())
    image = serializers.ImageField
    class Meta:
        model = Dish
        fields = [
            'id', 'name', 'category_id', 'energy_value', 'price',
            'image', 'category', 'allergens'
        ]
