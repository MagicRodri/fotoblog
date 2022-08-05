# Generated by Django 4.0.6 on 2022-08-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220805_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Creator'), ('SUBSCRIBER', 'Subscriber')], default='SUBSCRIBER', max_length=30),
        ),
    ]
