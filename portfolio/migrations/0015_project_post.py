# Generated by Django 3.2 on 2021-05-26 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment_email'),
        ('portfolio', '0014_remove_project_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_blog', to='blog.blog'),
        ),
    ]
