# Generated by Django 4.0.4 on 2022-05-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='head_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='head_slug',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='head_title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
