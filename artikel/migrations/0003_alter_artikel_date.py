# Generated by Django 4.1 on 2022-10-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0002_alter_artikel_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
