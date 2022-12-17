# Generated by Django 3.2.13 on 2022-12-17 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_collection_col_main_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='main_image',
            field=models.ImageField(default='./portfolio-1.jpg', upload_to='portfolio/'),
        ),
        migrations.AddField(
            model_name='project',
            name='collection_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.all_col'),
        ),
    ]