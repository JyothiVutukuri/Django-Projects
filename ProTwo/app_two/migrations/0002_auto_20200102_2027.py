# Generated by Django 2.2.5 on 2020-01-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]
