from django.urls import path
from .views import(
    upload_photo_view
)
urlpatterns = [
    path('upload/',upload_photo_view,name='upload-photo-view')
]
