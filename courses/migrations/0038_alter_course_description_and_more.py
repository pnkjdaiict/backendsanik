# Generated by Django 5.0 on 2024-12-01 10:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0037_remove_subcategory_subcourse_subcategory_subcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcourse',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]