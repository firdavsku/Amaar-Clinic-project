# Generated by Django 4.2.5 on 2024-11-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='phone',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
    ]
