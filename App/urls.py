from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.landing, name='landing'),
    path('products', views.products, name='products'),
    
    path('product_type', views.product_type, name='product_type'),
    path('product_search', views.product_search, name='product_search'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('basket', views.basket, name='basket'),
    path('destroy/<int:id>', views.destroy, name='destroy'),
] 
urlpatterns += staticfiles_urlpatterns()
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)