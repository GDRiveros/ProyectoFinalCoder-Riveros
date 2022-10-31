from calendar import c
from django.shortcuts import render
from BlogCoder.models import Blog, Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from BlogCoder.forms import UserEditionForm, AvatarForm
from django.contrib.auth.models import User

def mostrar_pagina_principal(request):
    return render(request, "BlogCoder/pagina_principal.html")

@login_required
def mostrar_inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except:
        avatar = None
    contexto = {"avatar": avatar}
    # avatar = Avatar.objects.get(user=request.user)
    # if avatar is not None:
    #     contexto = {"avatar": avatar.imagen.url}
    # else:
    #     contexto = {}
    return render(request, "BlogCoder/inicio.html", contexto)

@login_required
def vista_principal_de_blogs(request):
    return render(request, "BlogCoder/blogs/principal_blogs.html")

class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "BlogCoder/blogs/blog_list.html"

class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "BlogCoder/blogs/blog_detail.html"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha"]
    template_name = "BlogCoder/blogs/blog_form.html"

    def get_success_url(self): 
        return reverse("BlogList")

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "BlogCoder/blogs/blog_confirm_delete.html"

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

@login_required
def editar_perfil(request):

    #user = request.user

    # if request.method != "POST":
    #     form = UserEditionForm() # initial={"email": user.email}
    # else: 
    #     form = UserEditionForm(request.POST)

    #     if form.is_valid():
    #         data = form.cleaned_data
    #         user.email = data["email"]
    #         user.first_name = data["first_name"]
    #         user.last_name = data["last_name"]
    #         user.set_password(data["password1"])
    #         user.save()
    #         return render(request, "BlogCoder/inicio.html")

    # contexto = {"user": user, "form": form}
    # return render(request, "BlogCoder/editar_perfil.html", contexto)

    usuario = request.user

    if request.method == "POST":
        form = UserEditionForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return render(request, "BlogCoder/inicio.html")
    else: 
        form = UserEditionForm(instance=usuario)
    
    contexto = {"form": form}
    return render(request, "BlogCoder/user/editar_perfil.html", context=contexto)

@login_required
def listar_users(request):
    usuario = User.objects.all()
    contexto = {
        "usuarios": usuario,
    }

    return render(request, "BlogCoder/user/lista_users.html", contexto)

@login_required
def vista_principal_de_users(request):
    return render(request, "BlogCoder/user/principal_users.html")


class BorrarUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "BlogCoder/user/user_confirm_delete.html"

    def get_success_url(self): 
        return reverse("ListaUser")

@login_required
def agregar_avatar_al_user(request):
        if request.method != "POST":
            form = AvatarForm()
        else:
            form = AvatarForm(request.POST, request.FILES)
            if form.is_valid():
                Avatar.objects.filter(user=request.user).delete()
                form.save()
            return render(request, "BlogCoder/inicio.html")

        contexto = {"form": form}
        return render(request, "BlogCoder/avatars/avatar_form.html", contexto)
