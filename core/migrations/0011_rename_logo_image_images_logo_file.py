# Generated by Django 4.1.7 on 2023-09-29 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='logo_image',
            new_name='logo_file',
        ),
    ]
