# Generated by Django 4.1.7 on 2023-03-26 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chartapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='eid',
            new_name='title',
        ),
    ]
