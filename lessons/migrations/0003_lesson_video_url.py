# Generated by Django 5.1 on 2024-09-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Видео урока'),
        ),
    ]
