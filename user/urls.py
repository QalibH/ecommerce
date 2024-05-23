from django.urls import path
from user.views import register_view
from user.views import login_view
from user.views import logout_view
from user.views import profile_view

urlpatterns = [
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
]