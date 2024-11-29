# Generated by Django 5.0 on 2024-11-29 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_remove_course_subcourses_subcourse_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subcourses',
            field=models.ManyToManyField(blank=True, related_name='coursesnnn', to='courses.subcourse'),
        ),
    ]