from django.urls import path

from . import apis

urlpatterns = [
    
    path('createuser',apis.UserCreateAPIViewemail.as_view(), name='create-user'),
    path('<int:user_id>/update/', apis.UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:user_id>/delete/', apis.UserDeleteAPIView.as_view(), name='user-delete'),

    
    
]
