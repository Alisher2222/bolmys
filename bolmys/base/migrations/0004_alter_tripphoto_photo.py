# Generated by Django 4.2.5 on 2024-06-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_tripphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripphoto',
            name='photo',
            field=models.FileField(upload_to='trip_photos/'),
        ),
    ]
