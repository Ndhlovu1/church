# Generated by Django 4.2.5 on 2023-11-05 13:49

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_alter_blogdatabase_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogdatabase',
            options={'ordering': ('publish',)},
        ),
        migrations.AlterModelManagers(
            name='blogdatabase',
            managers=[
                ('publishedBlogs', django.db.models.manager.Manager()),
            ],
        ),
    ]
