from django.contrib.auth.models import Permission,Group


def set_user_group(user):
    
    #clear the existing groups of user
    user.groups.clear()
    if user.role == 'CREATOR':
        creators = Group.objects.get(name = 'creators')
        user.groups.add(creators)
    if user.role == 'SUBSCRIBER':
        subscribers = Group.objects.get(name = 'subscribers')
        user.groups.add(subscribers)

def set_photo_permissions(user):
    pass


def set_blog_permissions(user):
    pass