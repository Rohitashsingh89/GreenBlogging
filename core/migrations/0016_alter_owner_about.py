# Generated by Django 4.1.7 on 2023-09-29 23:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_owner_created_at_owner_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
