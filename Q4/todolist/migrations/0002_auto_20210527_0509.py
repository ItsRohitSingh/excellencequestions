# Generated by Django 3.1.3 on 2021-05-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='text',
        ),
        migrations.AddField(
            model_name='todo',
            name='EmailID',
            field=models.CharField(default='NULL', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='cname',
            field=models.CharField(default='NULL', max_length=50),
            preserve_default=False,
        ),
    ]
