# Generated by Django 3.2 on 2021-05-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210328_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cat',
            field=models.CharField(choices=[('user-interface', 'user-interface'), ('branding', 'branding'), ('mockup', 'mockup'), ('ui', 'ui')], default='ui', max_length=20),
        ),
    ]
