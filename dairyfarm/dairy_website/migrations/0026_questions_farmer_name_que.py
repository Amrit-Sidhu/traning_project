# Generated by Django 3.0.5 on 2020-05-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0025_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='farmer_name_que',
            field=models.CharField(default='Amritpal Singh', max_length=50),
        ),
    ]
