from django.urls import path
from .views import(
    upload_photo_view,
    create_post_view,
    post_detail_view,
)
urlpatterns = [
    path('create_post/',create_post_view,name='create-post-view'),
    path('post_detail/<slug:slug>/',post_detail_view,name='post-detail-view'),
    path('upload/',upload_photo_view,name='upload-photo-view')
]
