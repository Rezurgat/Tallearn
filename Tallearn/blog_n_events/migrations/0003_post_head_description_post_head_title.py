# Generated by Django 4.0.4 on 2022-05-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_n_events', '0002_post_head_slug_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='head_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]