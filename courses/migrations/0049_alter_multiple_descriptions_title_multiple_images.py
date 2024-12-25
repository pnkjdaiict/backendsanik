# Generated by Django 5.0 on 2024-12-25 04:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0048_alter_multiple_descriptions_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiple_descriptions",
            name="title",
            field=models.TextField(blank=True, default="new", null=True),
        ),
        migrations.CreateModel(
            name="multiple_Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=250, null=True)),
                ("image", models.ImageField(upload_to="course_images/")),
                ("image_alt", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("meta_title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "meta_description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("meta_keyword", models.TextField(blank=True, null=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="multiple_images",
                        to="courses.course",
                    ),
                ),
            ],
        ),
    ]