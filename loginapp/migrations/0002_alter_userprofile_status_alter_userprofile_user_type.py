# Generated by Django 5.1.3 on 2024-11-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('USER', 'User'), ('ADMIN', 'Admin'), ('RESTAURANT', 'Restaurant'), ('CAMP', 'Camp')], max_length=20),
        ),
    ]
