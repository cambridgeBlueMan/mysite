# Generated by Django 3.2.5 on 2022-10-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='food',
            new_name='foods',
        ),
    ]