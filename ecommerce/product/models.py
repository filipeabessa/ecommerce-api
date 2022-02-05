from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    responsible = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'product'


