from django.contrib import admin
from django.urls import path
from django.conf import settings

from financas.views import index, importar_csv

urlpatterns = [
    path("", index, name="index"),
    path("importar_csv", importar_csv, name="importar_csv"),
] 
