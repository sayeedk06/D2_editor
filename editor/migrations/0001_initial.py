# Generated by Django 3.2.2 on 2021-05-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('text_url_id', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
    ]