# Generated by Django 4.1.7 on 2023-03-04 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_about_about_about_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_ayanchery',
            new_name='about_description',
        ),
    ]
