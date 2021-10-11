from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.gestion_usuarios, name='gestion'),
    path('signup/', views.signup, name='signup'),
    path('detail/<int:id_usuario>', views.detail_usuario, name='detalle_usuario'),
]