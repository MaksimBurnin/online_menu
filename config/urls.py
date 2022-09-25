from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MenuView.as_view(), name='root'),
    #path('orders/', views.create_order, name='order:create'),
    path('orders/<int:order_id>', views.order, name='order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
