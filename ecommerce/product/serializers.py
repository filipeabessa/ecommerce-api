from django.utils import timezone
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    responsible = serializers.HiddenField(default=serializers.CurrentUserDefault())
    creation = serializers.DateTimeField(default=serializers.CreateOnlyDefault(timezone.now))
    class Meta:
        model = Product
        fields = ('id', 'title', 'content', 'price', 'creation', 'responsible')