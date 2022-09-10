from django.urls import path
from .views import(
    blog_home_view,
    create_post_view,
    post_detail_view,
    follows_view,
    follow,
    unfollow,
    post_edit_view
)
urlpatterns = [
    path('',blog_home_view,name='blog-home-view'),
    path('create_post/',create_post_view,name='create-post-view'),
    path('follows/',follows_view,name='follows-view'),
    path('follow/<str:username>',follow,name='follow'),
    path('post_detail/<slug:slug>/',post_detail_view,name='post-detail-view'),
    path('post_edit/<slug:slug>/',post_edit_view,name='post-edit-view'),
    path('unfollow/<str:username>',unfollow,name='unfollow'),
]
