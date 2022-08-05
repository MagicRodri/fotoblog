# Generated by Django 4.0.6 on 2022-08-05 21:25

from django.db import migrations

def set_blog_perms(apps,schema_editor):
    
    User = apps.get_model('accounts','User')
    Permission = apps.get_model('auth','Permission')
    Group = apps.get_model('auth','Group')

    add_post = Permission.objects.get(codename = 'add_post')
    change_post = Permission.objects.get(codename = 'change_post')
    delete_post = Permission.objects.get(codename = 'delete_post')
    view_post = Permission.objects.get(codename = 'view_post')

    creators = Group.objects.get(name = 'creators')
    subscribers = Group.objects.get(name = 'subscribers')

    subscribers.permissions.add(view_post)
    creators.permissions.add(add_post,change_post,delete_post,view_post)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_role'),
    ]

    operations = [
        migrations.RunPython(set_blog_perms)
    ]
