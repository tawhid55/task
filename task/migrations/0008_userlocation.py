# Generated by Django 2.2.5 on 2020-02-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]