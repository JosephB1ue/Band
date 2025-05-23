# Generated by Django 5.1.7 on 2025-04-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=100)),
                ('band_image', models.FileField(upload_to='band_images/')),
                ('band_description', models.TextField()),
            ],
        ),
    ]
