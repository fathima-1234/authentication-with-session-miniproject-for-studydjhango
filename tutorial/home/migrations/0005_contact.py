# Generated by Django 4.1.7 on 2023-03-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_place', models.TextField(max_length=250)),
                ('contact_date', models.DateField()),
            ],
        ),
    ]
