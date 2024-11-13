from django.urls import path
from .views import ( 
                    UsuarioLoginView, 
                    UsuarioListAPIView, 
                    UsuarioTokenListAPIView, 
                    UsuarioLogoutView, 
                    UsuarioCreateAPIView, 
                    UsuarioRetrieveAPIView, 
                    PermissionListAPIView, 
                    UsuarioPermissionUpdateAPIView, 
                    UsuarioGroupUpdateAPIView, 
                    UsuarioPermissionsAPIView
                    )

urlpatterns = [
    path('login/', UsuarioLoginView.as_view(), name='usuario-login'),
    path('logout/', UsuarioLogoutView.as_view(), name='usuario-logout'),
    path('tokens/', UsuarioTokenListAPIView.as_view(), name='token-list'),
    path('usuarios/', UsuarioListAPIView.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreateAPIView.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveAPIView.as_view(), name='usuario-detail'),

    path('permissions/', PermissionListAPIView.as_view(), name='permission-list'),
    path('user/<int:pk>/permissions/', UsuarioPermissionsAPIView.as_view(), name='user-permissions'),
    path('user/<int:pk>/permissions/update/', UsuarioPermissionUpdateAPIView.as_view(), name='user-permission-update'),
    path('user/<int:pk>/groups/', UsuarioGroupUpdateAPIView.as_view(), name='user-group-update'),
]