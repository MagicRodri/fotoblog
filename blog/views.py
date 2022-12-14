
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UploadPhotoForm, CreatePostForm , CommentForm
from .models import Photo,Post,Comment
from django.contrib.auth import get_user_model
from django.http import HttpResponse , JsonResponse
from django.db.models import Q
from itertools import chain
import json
# Create your views here.

User = get_user_model()


@login_required
def blog_home_view(request):
    user = request.user

    posts_lookup = Q(author__in = user.follows.all()) | Q(author = user)
    posts = Post.objects.filter(posts_lookup)
    
    photos_lookups = Q(uploader__in = user.follows.all()) | Q(uploader = user)
    photos = Photo.objects.filter(photos_lookups).exclude(post__in = posts)
    
    posts_and_photos = sorted(chain(posts,photos),key=lambda instance : instance.timestamp,reverse = True)
    context = {
        'posts_and_photos' : posts_and_photos,
        'photos': photos,
        'posts' : posts
    }
    return render(request,'blog/blog_home.html',context = context)

# @login_required
# @permission_required('blog.add_photo',raise_exception=True)
# def upload_photo_view(request):

#     form = UploadPhotoForm()
#     if request.method == 'POST':
#         form = UploadPhotoForm(request.POST,request.FILES)

#         if form.is_valid():
#             photo=form.save(commit=False)
#             photo.uploader = request.user
#             photo.save()
#             return redirect(reverse('home-view'))

#     return render(request,'blog/upload_photo.html',context={'form':form})

@login_required
@permission_required('blog.add_post',raise_exception=True)
def create_post_view(request):
    user = request.user
    photo_form = UploadPhotoForm()
    post_form = CreatePostForm()
    if request.method == 'POST':
        photo_form = UploadPhotoForm(request.POST,request.FILES)
        post_form = CreatePostForm(request.POST)
        if all([photo_form.is_valid(),post_form.is_valid()]):
            photo =  photo_form.save(commit=False) # retrieve the photo without pushing into the db
            photo.uploader = user # Set the uploader
            photo.save() # Push to the db

            # Same procedure for the post instance
            post = post_form.save(commit=False)
            post.photo = photo
            post.author = user
            post.save()

            return redirect(reverse('blog-home-view'))

    context = {
        'photo_form':photo_form,
        'post_form':post_form
    }
    return render(request,'blog/create_post.html',context=context)
@login_required
def post_detail_view(request,slug=None):
    post = None
    data = {}
    context = {}
    comment_form = CommentForm()

    if slug is not None:
        post = get_object_or_404(Post,slug=slug)
        context['post']=post
        comments = Comment.objects.filter(post = post)
        context['comments'] = comments

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = context.get('post')
        comment.save()
        
        data['username'] = request.user.username
        data['content'] = comment.content

        return JsonResponse(data=data)
        # return redirect(comment.post.get_absolute_url())

    context['comment_form'] = comment_form
    return render(request,'blog/post_detail.html',context=context)

@login_required
def follows_view(request):
    
    online_user = request.user
    online_user_follows = online_user.follows.all()

    #exclude the online user if he is a creator
    creators = User.objects.filter(role = 'CREATOR').exclude(username = online_user.username)

    #fetch the non following creators
    creators = creators.difference(online_user_follows)

    # Note : exlude after difference is not supported
    if request.method == 'POST':
        username = request.POST.get('username')
        creator = get_object_or_404(User,username = username)
        online_user.add_follow(creator)
        return redirect(reverse('follows-view'))

    return render(request,'blog/follows.html',context={'creators':creators})

@login_required
def follow(request,username):
    try:
        follow = User.objects.get(username=username)
        request.user.add_follow(follow)
        return redirect(reverse('follows-view'))
    except:
        ...
    return HttpResponse('Following unsuccessful')
        
@login_required
def unfollow(request,username):
    try:
        follow = User.objects.get(username=username)
        request.user.remove_follow(follow)
        return redirect(reverse('profile-view'))
    except:
        ...
    return HttpResponse("Unfollowing unsuccessful")

@login_required
def post_edit_view(request,slug = None):
    user = request.user
    if slug:
        try :
            post = Post.objects.get(slug = slug)
        except:
            ...
    if not user.has_perm('change_post',post):
        return HttpResponse('You can not access this page!')

    photo_form = UploadPhotoForm(instance= post.photo)
    post_form = CreatePostForm(instance=post)
    if request.method == 'POST':
        photo_form = UploadPhotoForm(request.POST,request.FILES,instance = post.photo)
        post_form = CreatePostForm(request.POST, instance = post)
        if all([photo_form.is_valid(),post_form.is_valid()]):
            photo =  photo_form.save(commit=False)
            photo.uploader = user
            photo.save() 

            # Same procedure for the post instance
            post = post_form.save(commit=False)
            post.photo = photo
            photo.author = user
            post.save()

            return redirect(reverse('blog-home-view'))
    return render(request, 'blog/edit_post.html',context={
        'photo_form' : photo_form,
        'post_form' : post_form
    })