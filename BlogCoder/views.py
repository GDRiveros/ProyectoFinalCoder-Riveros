from calendar import c
from django.shortcuts import render
from BlogCoder.models import Blog
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from BlogCoder.forms import UserEditionForm
from django.contrib.auth.models import User

def mostrar_pagina_principal(request):
    return render(request, "BlogCoder/pagina_principal.html")

@login_required
def mostrar_inicio(request):
    usuario = User.objects.all()
    return render(request, "BlogCoder/inicio.html")

@login_required
def vista_principal_de_blogs(request):
    return render(request, "BlogCoder/principal_blogs.html")

class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "BlogCoder/blog_list.html"

class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "BlogCoder/blog_detail.html"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha"]

    def get_success_url(self): 
        return reverse("BlogList")

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog

    def get_success_url(self): 
        return reverse("BlogList")

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha"]
    success_url = "/blogcoder/blog-list"

def register(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()
            return render(request, "BlogCoder/inicio.html")

    else:
        form = UserCreationForm()

    return render(request, "BlogCoder/registro.html", {"form": form})
    
class MyLogin(LoginView):
    template_name = "BlogCoder/login.html"

class MyLogout (LogoutView):
    template_name = "BlogCoder/logout.html"


def editar_perfil(request):

    user = request.user

    if request.method != "POST":
        form = UserEditionForm() # initial={"email": user.email}
    else: 
        form = UserEditionForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "BlogCoder/inicio.html")

    contexto = {"user": user, "form": form}
    return render(request, "BlogCoder/editar_perfil.html", contexto)

def listar_users(request):
    usuario = User.objects.all()
    contexto = {
        "usuarios": usuario,
    }

    return render(request, "BlogCoder/lista_users.html", contexto)

def vista_principal_de_users(request):
    return render(request, "BlogCoder/principal_users.html")


#class BorrarUser(DeleteView):
    #model = User

    #def get_success_url(self): 
    #    return reverse("ListaUser")
