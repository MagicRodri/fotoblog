from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup_view,
    profile_view,
    upload_pp_view,
    edit_profile_view,
)

urlpatterns = [
    path('edit_profile',edit_profile_view,name='edit-profile-view'),
    path('login/',login_view,name='login-view'),
    path('logout/',logout_view,name='logout-view'),
    path('upload_pp/',upload_pp_view,name='upload-pp-view'),
    path('profile/',profile_view,name='profile-view'),
    path('signup/',signup_view,name='signup-view')
]
