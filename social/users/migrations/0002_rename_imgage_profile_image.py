# Generated by Django 3.2 on 2021-04-20 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='imgage',
            new_name='image',
        ),
    ]
