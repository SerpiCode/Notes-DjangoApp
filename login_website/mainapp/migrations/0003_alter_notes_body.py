# Generated by Django 4.1.1 on 2022-11-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_notes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='body',
            field=models.TextField(max_length=255),
        ),
    ]