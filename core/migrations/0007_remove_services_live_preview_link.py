# Generated by Django 4.1.7 on 2023-09-29 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_services_delete_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='live_preview_link',
        ),
    ]