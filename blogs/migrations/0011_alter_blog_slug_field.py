# Generated by Django 5.0 on 2024-12-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0010_alter_blog_slug_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug_field",
            field=models.SlugField(default="slug_Blog"),
        ),
    ]
