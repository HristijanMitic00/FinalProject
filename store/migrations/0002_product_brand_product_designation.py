# Generated by Django 4.2.4 on 2023-08-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
