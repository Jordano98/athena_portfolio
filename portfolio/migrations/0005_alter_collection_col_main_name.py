# Generated by Django 3.2.13 on 2022-12-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_collection_col_main_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='col_main_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]