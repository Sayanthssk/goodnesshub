# Generated by Django 5.1.3 on 2024-11-12 07:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_campregistrationmodel_login_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Restaurant_model',
        ),
    ]
