# Generated by Django 4.1 on 2022-08-25 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0003_remove_posts_img_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
