from django.contrib import admin

# Register your models here.

from BlogCoder.models import Blog, Autor

admin.site.register(Blog)
admin.site.register(Autor)
