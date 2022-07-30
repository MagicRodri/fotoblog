from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import (
    login_view,
    logout_view,
    signup_view,
)

urlpatterns = [
    path('login/',login_view,name='login-view'),
    path('logout/',logout_view,name='logout-view'),
    path('signup/',signup_view,name='signup-view')
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)