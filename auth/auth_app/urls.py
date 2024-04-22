from django.urls import path
from .views import login, profile, phone_login, phone_login_code

urlpatterns = [
    path(r'', phone_login, name='phone_login'),
    path('phone_login/', phone_login, name='phone_login'),
    path('phone_login_code/', phone_login_code, name='phone_login_code'),

    path('profile/', profile, name='profile'),
]
