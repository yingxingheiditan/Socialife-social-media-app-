# Generated by Django 4.1 on 2022-08-25 05:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0004_alter_posts_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
