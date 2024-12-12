# Generated by Django 5.0 on 2024-12-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "homepage",
            "0013_remove_enquiryform_cities_remove_enquiryform_states_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="seo",
            name="address",
            field=models.CharField(
                blank=True,
                help_text="The home Page Title of the page.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="seo",
            name="contact_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="seo",
            name="email",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
