# Generated by Django 4.1.2 on 2023-02-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=255)),
                ('data', models.FileField(upload_to='async-kv-table')),
            ],
        ),
    ]