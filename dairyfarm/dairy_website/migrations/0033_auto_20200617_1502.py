# Generated by Django 3.0.5 on 2020-06-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0032_auto_20200609_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_record',
            name='farmer_id',
            field=models.IntegerField(max_length=50),
        ),
    ]
