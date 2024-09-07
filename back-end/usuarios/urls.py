from django.urls import path
from .views import UsuarioLoginView, UsuarioListAPIView, UsuarioTokenListAPIView, UsuarioLogoutView, UsuarioCreateAPIView, UsuarioRetrieveAPIView


urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('token/', UsuarioTokenListAPIView.as_view(), name='token-list'),
    path('logout/<str:pk>', UsuarioLogoutView.as_view(), name='user-login'),

    path('usuarios/list/', UsuarioListAPIView.as_view(), name='usuarios-list'),
    path('usuario/create/', UsuarioCreateAPIView.as_view(), name='usuario-create'),
    path('usuario/detail/<int:pk>', UsuarioRetrieveAPIView.as_view(), name='usuario-detail')
]