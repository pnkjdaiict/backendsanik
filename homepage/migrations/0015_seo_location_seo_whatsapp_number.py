# Generated by Django 5.0 on 2024-12-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0014_seo_address_seo_contact_number_seo_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="seo",
            name="location",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="seo",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
