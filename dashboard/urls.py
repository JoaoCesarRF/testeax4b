"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_vendas.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('nova_venda', nova_venda, name='nova_venda'),
    path('cadastro_cliente', cadastro_cliente, name='cad_cliente'),
    path('cadastro_produto', cadastro_produto, name='cad_prod'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard_clientes', dashboard_clientes, name='dashboard_clientes'),
    path('dashboard_produtos', dashboard_produtos, name='dashboard_produtos'),
    path('update/<int:pk>/', vendas_update, name='update'),
    path('delete/<int:pk>/', vendas_delete, name='delete'),
    path('clientes_update/<int:pk>/', clientes_update, name='clientes_update'),
    path('produtos_update/<int:pk>/', produtos_update, name='produtos_update'),
]
