from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup_view,
    profile_view
)

urlpatterns = [
    path('login/',login_view,name='login-view'),
    path('logout/',logout_view,name='logout-view'),
    path('profile/',profile_view,name='profile-view'),
    path('signup/',signup_view,name='signup-view')
]
