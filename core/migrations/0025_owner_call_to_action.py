# Generated by Django 4.1.7 on 2023-09-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_rename_blog_headinng_owner_blog_heading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='call_to_action',
            field=models.CharField(default="Let's have a one to one session with me.", max_length=300),
        ),
    ]
