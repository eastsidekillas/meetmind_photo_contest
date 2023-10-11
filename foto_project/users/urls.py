from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
]