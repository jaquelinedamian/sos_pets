from django.contrib import admin

# Register your models here.
# core/admin.py
from django.contrib import admin
from .models import Usuarios

admin.site.register(Usuarios)
