# Generated by Django 3.2.7 on 2021-09-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='development',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=9, editable=False, max_digits=15),
        ),
        migrations.AlterField(
            model_name='development',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=9, editable=False, max_digits=15),
        ),
        migrations.AlterField(
            model_name='development',
            name='property_manager_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='development',
            name='property_manager_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]