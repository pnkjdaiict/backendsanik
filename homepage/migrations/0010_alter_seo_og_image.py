# Generated by Django 5.1.3 on 2024-11-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
