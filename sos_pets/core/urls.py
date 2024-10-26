from django.urls import path
from . import views
from .views import cadastro

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # Defina as demais rotas
    path('vitrine/', views.vitrine, name='vitrine'), 
    path('login/', views.login, name='login')  # Remova a vírgula final aqui
]
