# Generated by Django 4.2.7 on 2024-01-23 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_alter_comment_options_remove_post_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='edit_mode',
        ),
    ]
