# Generated by Django 3.2.7 on 2021-09-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developments', '0005_auto_20210924_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='development',
            name='img',
        ),
        migrations.AddField(
            model_name='development',
            name='full_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/full/'),
        ),
        migrations.AddField(
            model_name='development',
            name='thumbnail_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/thumbnail/'),
        ),
    ]
