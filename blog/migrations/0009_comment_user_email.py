# Generated by Django 3.0.3 on 2021-04-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(default='', max_length=70),
        ),
    ]
