"""testUseIt URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from core import views as core_views
from rest_framework import routers
from empresa import views as empresa_views
from empresaCliente import views as empresaCliente_views
from contacto import views as contacto_views
from oportunidad import views as oportunidad_views

router = routers.DefaultRouter()
router.register(r'users', core_views.UserViewSet)
router.register(r'groups', core_views.GroupViewSet)
router.register(r'empresa', empresa_views.EmpresaViewSet)
router.register(r'usuario_empresa', empresa_views.UsuariosEmpresaViewSet)
router.register(r'empresas_clientes', empresaCliente_views.EmpresaClienteViewSet)
router.register(r'contactos', contacto_views.ContactoViewSet)
router.register(r'oportunidades', oportunidad_views.OportunidadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('empresas/', include('empresa.urls')),
    path('empresas_clientes/', include('empresaCliente.urls')),
    path('contactos/', include('contacto.urls')),
    path('oportunidades/', include('oportunidad.urls')),
    path('core/', include('core.urls')),
    path('api/', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)