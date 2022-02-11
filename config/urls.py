from django.contrib import admin
from django.urls import path, include
from ecommerce.docs import urlpatterns as docs_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ecommerce.product.urls')),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("", include(docs_urls)),
]
