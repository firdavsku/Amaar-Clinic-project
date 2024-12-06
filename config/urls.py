from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from app.views import switch_language
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('switch-language/', switch_language, name='switch_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
)