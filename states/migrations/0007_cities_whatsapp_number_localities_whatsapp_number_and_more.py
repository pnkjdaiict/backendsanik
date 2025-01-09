# Generated by Django 5.0 on 2025-01-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("states", "0006_state_whatsapp_number_state_youtube_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cities",
            name="whatsapp_number",
            field=models.CharField(
                blank=True, default="8278640248", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="localities",
            name="whatsapp_number",
            field=models.CharField(
                blank=True, default="8278640248", max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="localities",
            name="youtube_link",
            field=models.CharField(
                blank=True,
                default="https://www.youtube.com/@rdajaipur",
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="localities",
            name="contact_number",
            field=models.CharField(
                blank=True, default="8769422006", max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="localities",
            name="facebook_link",
            field=models.CharField(
                blank=True,
                default="https://www.facebook.com/Sainikschoolentranceexamcoaching/",
                max_length=250,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="localities",
            name="instagram_link",
            field=models.CharField(
                blank=True,
                default="https://www.instagram.com/onlinesainikschoolcoaching/",
                max_length=250,
                null=True,
            ),
        ),
    ]