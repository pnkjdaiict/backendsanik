# Generated by Django 5.0 on 2024-12-26 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0052_alter_multiple_images_course"),
    ]

    operations = [
        migrations.RenameField(
            model_name="multiple_images", old_name="image", new_name="imagess",
        ),
    ]
