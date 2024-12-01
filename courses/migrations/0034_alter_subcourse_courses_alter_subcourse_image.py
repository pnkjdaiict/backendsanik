# Generated by Django 5.0 on 2024-12-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0033_alter_subcourse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcourse',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='coursesnn', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='subcourse',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcourse/'),
        ),
    ]
