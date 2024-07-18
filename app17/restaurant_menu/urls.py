from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import MenuItemDetail, MenuList

urlpatterns = [
    path('', MenuList.as_view(), name='menu_list'),
    path('item/<int:pk>',MenuItemDetail.as_view(),name='menu_item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
