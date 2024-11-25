# Generated by Django 5.1.3 on 2024-11-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('RESTAURANT', 'Restaurant'), ('USER', 'User'), ('CAMP', 'Camp')], max_length=20),
        ),
    ]
