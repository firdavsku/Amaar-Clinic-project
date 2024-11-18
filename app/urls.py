from django.urls import path
from . import views
from app.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('about_us/', views.about_view, name='about_us'),
    path('departments/', views.departments_view, name='department'),
    path('doctors/', views.doctors_view, name='doctors'),

]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 
