# Generated by Django 3.1.4 on 2021-08-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210804_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='accuracy_feed',
            field=models.CharField(default=5, max_length=5),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='experience_feed',
            field=models.CharField(default=5, max_length=5),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='recommend_feed',
            field=models.CharField(default=5, max_length=5),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='uage',
            field=models.CharField(default='', max_length=5),
        ),
    ]
