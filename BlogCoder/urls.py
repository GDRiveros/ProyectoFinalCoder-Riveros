"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from BlogCoder.views import (
    mostrar_inicio,
    vista_principal_de_blogs,
    BlogList,
    BlogDetail,
    BlogUpdateView,
    BlogDelete,
    BlogCreate,
    register,
    MyLogin,
    MyLogout,
    mostrar_pagina_principal,
    editar_perfil,
    listar_users,
    vista_principal_de_users,
    agregar_avatar_al_user,
    BorrarUser,
    contar_sobre_mi,
    AutorCreate,
    AutorUpdateView,
    AutorDelete,
    AutorList,
    AutorDetail,
)

urlpatterns = [
    path("", mostrar_pagina_principal, name="PaginaPrincipal"),
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("blogs/", vista_principal_de_blogs, name="Blogs"),
    path("pages/", BlogList.as_view(), name="BlogList"),
    path("blog-detalle/<pk>'", BlogDetail.as_view(), name="BlogDetail"),
    path("editar/<pk>", BlogUpdateView.as_view(), name="BlogUpdate"),
    path("borrar/<pk>", BlogDelete.as_view(), name="BlogDelete"),
    path("new-blog/", BlogCreate.as_view(), name="BlogCreate"),
    path("accounts/signup/", register, name="Register"),
    path("accounts/login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("accouts/profile/", listar_users, name="ListaUser"),
    path("users/", vista_principal_de_users, name="Users"),
    path("delete-user/<pk>", BorrarUser.as_view(), name="UserDelete"),
    path("agregar-avatar/", agregar_avatar_al_user, name="AgregarAvatar"),
    path("about/", contar_sobre_mi),
    path("crear-autor/", AutorCreate.as_view(), name="CreacionAutor"),
    path("editar-autor/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),
    path("borrar-autor/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    path("ver-autores/", AutorList.as_view(), name="AutorList"),
    path("autor-detalle/<pk>'", AutorDetail.as_view(), name="AutorDetail"),
]
