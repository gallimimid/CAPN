# Generated by Django 2.0.1 on 2018-01-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180107_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_mnt',
            name='pid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_mnt',
            name='pid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
