# Generated by Django 5.0 on 2024-11-27 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_subcourse_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcourse',
            old_name='feature_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='subcourse',
            name='img',
        ),
    ]
