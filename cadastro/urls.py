from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',include('usuario.urls')),
    path('usuario/',include('login.urls')),
    path('',lambda request:redirect('/usuario/login')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
