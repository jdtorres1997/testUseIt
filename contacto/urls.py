from django.urls import path

from . import views

app_name = 'contactos'
urlpatterns = [
    path('', views.gestion_contactos, name='gestion'),
    path('add', views.add_contacto, name='crear_contacto'),
    path('edit/<int:id_contacto>', views.editar_contacto, name='modificar_contacto'),
    path('delete/<int:id_contacto>', views.eliminar_contacto, name='eliminar_contacto'),
    path('detail/<int:id_contacto>', views.detail_contacto, name='detalle_contacto'),
]