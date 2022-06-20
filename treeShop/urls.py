from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('account/', include('account.urls', namespace='account')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('loaderio-34f424f22d6a6db5c7287532478f4b19/')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
