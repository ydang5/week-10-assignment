# Generated by Django 2.2.6 on 2019-11-09 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0002_militarydb_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='militarydb',
            old_name='test',
            new_name='name',
        ),
    ]