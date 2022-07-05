from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path("marca/cadastrar/", views.cadastrar_marca, name="cadastrar_marca"),
    path("marca/listar/", views.listar_marca, name="listar_marca"),
    path("marca/editar/<int:pk>/", views.editar_marca, name="editar_marca"),
    path("marca/produto/<int:pk>/", views.listar_produtos_marca, name="marca_produto"),
    path("marca/remover/<int:pk>/", views.remover_marca, name="remover_marca"),

    path("produto/cadastrar/", views.cadastrar_produto, name="cadastrar_produto"),
    path("produto/listar/", views.listar_produto, name="listar_produto"),
    path("produto/editar/<int:pk>/", views.editar_produto, name="editar_produto"),
    path("produto/remover/<int:pk>/", views.remover_produto, name="remover_produto"),
    path("produto/perfil/<int:pk>/", views.perfil_produto, name='perfil_produto'),


    path("categoria/cadastrar/", views.cadastrar_categoria, name="cadastrar_categoria"),
    path("categoria/listar", views.listar_categoria, name='listar_categoria'),
    path("categoria/editar/<int:pk>/", views.editar_categoria, name="editar_categoria"),
    path("categoria/remover/<int:pk>/", views.remover_categoria, name="remover_categoria"),
    path("categoria/produto/<int:pk>/", views.listar_produtos_categoria, name="categoria_produto"),
]
