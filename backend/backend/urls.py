from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from presenca.views import AlunoViewSet, PresencaViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'presencas', PresencaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
