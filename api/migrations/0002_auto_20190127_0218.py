# Generated by Django 2.0.8 on 2019-01-27 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Abstract',
            new_name='Base',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='abstract_ptr',
            new_name='base_ptr',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='abstract_ptr',
            new_name='base_ptr',
        ),
    ]