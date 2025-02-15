# Generated by Django 5.0 on 2025-02-13 05:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0055_rename_image_multiple_images_imagess"),
        ("homepage", "0022_faq_course_alter_faq_answer_alter_faq_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="enquiryform",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="faq",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="Leave blank for homepage",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="faqs",
                to="courses.course",
            ),
        ),
    ]
