# Generated by Django 4.1.4 on 2022-12-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
