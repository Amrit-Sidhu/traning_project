# Generated by Django 3.0.5 on 2020-04-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0019_milk_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal_record',
            name='farmer_id',
            field=models.CharField(default='just added', max_length=50),
        ),
    ]
