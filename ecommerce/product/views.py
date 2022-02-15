from rest_framework import viewsets
from decimal import Decimal




from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title', None)
        price = self.request.query_params.get('price', None)
        
        if (title is not None):
            queryset = queryset.filter(title__icontains=title)
            
        if (price is not None):
            queryset = queryset.filter(price=Decimal(price))
        
        return queryset
