from django.contrib import admin
from .models import Aluno, Presenca

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Presenca)