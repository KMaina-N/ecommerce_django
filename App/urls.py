from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product_type', views.product_type, name='product_type'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('basket', views.basket, name='basket'),
    path('destroy/<int:id>', views.destroy, name='destroy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)