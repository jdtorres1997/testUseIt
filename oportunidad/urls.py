from django.urls import path

from . import views

app_name = 'oportunidades'
urlpatterns = [
    path('', views.gestion_oportunidades, name='gestion'),
    path('add', views.add_oportunidad, name='crear_oportunidad'),
    path('edit/<int:id_oportunidad>', views.editar_oportunidad, name='modificar_oportunidad'),
    path('delete/<int:id_oportunidad>', views.eliminar_oportunidad, name='eliminar_oportunidad'),
    path('detail/<int:id_oportunidad>', views.detail_oportunidad, name='detalle_oportunidad'),
]