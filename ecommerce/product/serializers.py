from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    responsible = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = ('id', 'title', 'content', 'price', 'creation', 'responsible')