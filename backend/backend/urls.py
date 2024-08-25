from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs from users/urls/Userurls.py
    path('api/', include('backend.users.urls.Usersurls')),
     path('api/', include('backend.users.urls.Customerurls')), 
     path('api/',include('backend.products.urls.ProductUrls')),
     path('api/',include('backend.orders.urls.OrderUrls'))
]