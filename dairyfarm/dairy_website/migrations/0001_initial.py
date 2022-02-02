# Generated by Django 3.0.5 on 2020-04-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('farm_name', models.CharField(max_length=50)),
                ('farm_type', models.CharField(max_length=50)),
                ('total_animal', models.CharField(max_length=20)),
            ],
        ),
    ]
