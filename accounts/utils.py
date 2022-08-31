from django.contrib.auth.models import Permission,Group
from guardian.shortcuts import assign_perm

def set_user_group(user):
    
    #clear the existing groups of user
    user.groups.clear()

    if user.role == 'CREATOR':
        creators = Group.objects.get(name = 'creators')
        user.groups.add(creators)
    if user.role == 'SUBSCRIBER':
        subscribers = Group.objects.get(name = 'subscribers')
        user.groups.add(subscribers)

def set_profile_edit_permission(user):
    #Assign user change permission to a user for his own user obj

    if not user.has_perm('change_user',user):
        assign_perm('change_user',user,obj=user)