# Generated by Django 5.0 on 2024-11-29 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_remove_course_subcourses_course_subcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='SubCourse',
        ),
        migrations.RemoveField(
            model_name='subcourse',
            name='courses',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='subcourse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='courses.subcourse'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcourse',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='subcourse',
            name='short_description',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='course_images/')),
                ('image_alt', models.CharField(blank=True, max_length=250, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='courses.course')),
            ],
        ),
    ]