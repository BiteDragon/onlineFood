# Generated by Django 5.1.4 on 2025-01-03 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_created_at_alter_user_date_joined_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='user/profile_picture')),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='users/cover_photo')),
                ('address_line1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('longitude', models.CharField(blank=True, max_length=30, null=True)),
                ('latitude', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
