from django.urls import path, re_path
from .views import *

urlpatterns = [
    # home - псевдоним для указания домашней страницы
    path('', index, name='home'),                # http://127.0.0.1:8000/women
    path("cats/<int:cat>/", categories),       # http://127.0.0.1:8000/cats/1
    # path("cats/<slug:cat>/", categories)       # http://127.0.0.1:8000/cats/1
    re_path(r'archive/(?P<year>[0-9]{4})', archive)
]
