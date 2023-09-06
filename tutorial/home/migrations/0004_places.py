# Generated by Django 4.1.7 on 2023-03-04 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_about_ayanchery_about_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places_title', models.CharField(max_length=100)),
                ('places_description', models.TextField()),
                ('places_image', models.ImageField(upload_to='Places')),
            ],
        ),
    ]