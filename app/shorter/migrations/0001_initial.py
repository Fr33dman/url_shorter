# Generated by Django 3.1.7 on 2021-05-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_url', models.URLField()),
                ('key', models.CharField(max_length=7, unique=True)),
            ],
        ),
    ]
