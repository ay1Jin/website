# Generated by Django 2.2 on 2020-11-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermanager', '0002_auto_20201124_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picmanage',
            name='isShow',
            field=models.CharField(choices=[('1', 'show'), ('0', 'unshow')], max_length=1, verbose_name='是否显示'),
        ),
        migrations.AlterField(
            model_name='picmanage',
            name='path',
            field=models.CharField(max_length=100, verbose_name='路径'),
        ),
        migrations.AlterField(
            model_name='picmanage',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='picmanage',
            name='title',
            field=models.CharField(default='图片.jpg', max_length=100, verbose_name='标题'),
        ),
    ]
