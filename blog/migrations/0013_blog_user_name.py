# Generated by Django 3.2 on 2021-05-24 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20210524_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.ForeignKey(default='root', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
