from django.urls import path
from . import views
from app.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 
