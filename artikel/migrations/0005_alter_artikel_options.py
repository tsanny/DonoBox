# Generated by Django 4.1 on 2022-10-31 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0004_alter_artikel_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-date']},
        ),
    ]
