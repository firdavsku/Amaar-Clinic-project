from django.urls import path
from . import views
from app.views import IndexView,switch_language
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# url
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('about_us/', views.about_view, name='about_us'),
    path('departments/', views.departments_view, name='department'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('services/', views.ServicesListView.as_view(), name='services_list'),
    path('switch_language/', views.switch_language, name='switch_language'),
]

 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
 
