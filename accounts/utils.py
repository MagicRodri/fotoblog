from django.contrib.auth.models import Permission,Group


def set_user_group(user):
    creators = Group.objects.get(name = 'creators')
    subscribers = Group.objects.get(name = 'subscribers')
    #clear the existing groups of user
    user.groups.clear()
    if user.role == 'CREATOR':
        user.groups.add(creators)
    if user.role == 'SUBSCRIBER':
        user.groups.add(subscribers)

def set_photo_permissions(user):
    pass


def set_blog_permissions(user):
    pass