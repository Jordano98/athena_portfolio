# Generated by Django 3.2.13 on 2022-12-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_remove_collection_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='gallery',
        ),
        migrations.AddField(
            model_name='project',
            name='main_image',
            field=models.ImageField(default='./portfolio-1.jpg', upload_to='portfolio/'),
        ),
    ]
