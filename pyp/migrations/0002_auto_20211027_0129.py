# Generated by Django 3.2.8 on 2021-10-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorylist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
