from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'dishes', views.ApiDishViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MenuView.as_view(), name='root'),
    path('orders/<int:order_id>', views.order, name='order'),
    path('cart', views.cart_action),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
