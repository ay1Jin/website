# Generated by Django 2.2 on 2020-11-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picmanage',
            name='path',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='picmanage',
            name='title',
            field=models.CharField(default='图片.jpg', max_length=100),
        ),
    ]
