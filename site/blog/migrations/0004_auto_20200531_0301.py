# Generated by Django 3.0.3 on 2020-05-31 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_code_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]