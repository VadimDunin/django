"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from coolsite import settings
from women.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),                    # http://127.0.0.1:8000/admin
    path('', include("women.urls")),              # http://127.0.0.1:8000/women
    path('about', about, name='about'),              # http://127.0.0.1:8000/women
]

# Обработчики работают только, если дебаг режим джанго выключен
handler404 = pageNotFound

# ToDo - написать свои обработчики для остальных ошибок
# handler500 = internalServerError
# handler403 = accessDenied
# handler400 = unableExecRecuest

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
