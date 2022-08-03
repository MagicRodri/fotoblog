from django.urls import path
from .views import(
    upload_photo_view,
    create_post_view,
)
urlpatterns = [
    path('create_post/',create_post_view,name='create-post-view'),
    path('upload/',upload_photo_view,name='upload-photo-view')
]
