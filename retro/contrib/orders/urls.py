from django.urls import path
from django.conf import settings
from djamgo.cong.urls.static import static

from . import views


urlpatterns = [
    path('za-vkshi/<int:item_id>', views.Stuff.as_view(), name='za-vkshi')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)