# Generated by Django 5.0 on 2024-12-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0018_alter_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog", name="slug", field=models.SlugField(max_length=255),
        ),
    ]