# Generated by Django 4.1.4 on 2022-12-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_comment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.URLField(null=True),
        ),
    ]
