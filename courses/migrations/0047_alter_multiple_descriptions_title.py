# Generated by Django 5.0 on 2024-12-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0046_multiple_descriptions_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiple_descriptions",
            name="title",
            field=models.TextField(blank=True, default="title", null=True),
        ),
    ]
