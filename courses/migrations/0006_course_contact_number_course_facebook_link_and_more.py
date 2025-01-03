# Generated by Django 5.1.3 on 2024-11-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_subcourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='contact_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='contact_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='meta_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='meta_keyword',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='meta_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
