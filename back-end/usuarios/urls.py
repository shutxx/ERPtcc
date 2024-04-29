from django.urls import path
from .views import UsuarioLoginView, UsuarioListAPIView, UsuarioTokenListAPIView, UsuarioLogoutView, UsuarioCreateAPIView


urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('usuarios/list/', UsuarioListAPIView.as_view(), name='usuarios-list'),
    path('usuario/create/', UsuarioCreateAPIView.as_view(), name='usuarios-create'),
    path('token/', UsuarioTokenListAPIView.as_view(), name='token-list'),
    path('logout/<str:pk>', UsuarioLogoutView.as_view(), name='user-login')
]