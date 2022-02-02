# Generated by Django 3.0.5 on 2020-04-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0004_animal_reord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal_reord',
            old_name='cattle_inseminated',
            new_name='is_cattle_inseminated',
        ),
        migrations.RemoveField(
            model_name='animal_reord',
            name='animal_type',
        ),
        migrations.AddField(
            model_name='animal_reord',
            name='bull_details',
            field=models.CharField(default=None, max_length=50),
        ),
    ]