# Generated by Django 5.1.3 on 2024-12-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='headline_en',
            field=models.TextField(blank=True, null=True, verbose_name='Headline Text (EN)'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='headline_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Headline Text (KK)'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='headline_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Headline Text (RU)'),
        ),
    ]