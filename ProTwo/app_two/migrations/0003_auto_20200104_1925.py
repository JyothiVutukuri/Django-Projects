# Generated by Django 2.2.5 on 2020-01-04 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0002_auto_20200102_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
    ]
