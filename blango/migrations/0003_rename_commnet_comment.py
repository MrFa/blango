# Generated by Django 3.2.5 on 2021-12-27 12:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('blango', '0002_commnet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnet',
            new_name='Comment',
        ),
    ]
