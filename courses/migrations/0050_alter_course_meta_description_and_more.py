# Generated by Django 5.0 on 2024-12-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0049_alter_multiple_descriptions_title_multiple_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="meta_description",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="meta_title",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
