# Generated by Django 3.0.5 on 2020-05-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0028_auto_20200511_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='que_id',
            field=models.IntegerField(),
        ),
    ]