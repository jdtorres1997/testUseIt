from django.urls import path

from . import views

app_name = 'empresa'
urlpatterns = [
    path('', views.gestion_empresas, name='gestion'),
    path('add', views.add_empresa, name='crear_empresa'),
    path('edit/<int:id_empresa>', views.editar_empresa, name='modificar_empresa'),
    path('delete/<int:id_empresa>', views.eliminar_empresa, name='eliminar_empresa'),
    path('detail/<int:id_empresa>', views.detail_empresa, name='detalle_empresa'),
    path('detail/<int:id_empresa>/vincular/', views.vincular_usuario, name='vincular_usuario'),
    path('detail/<int:id_empresa>/desvincular/<int:id_usuario>', views.eliminar_usuario, name='desvincular_usuario'),
]