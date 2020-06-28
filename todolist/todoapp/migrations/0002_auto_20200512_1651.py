# Generated by Django 3.0.3 on 2020-05-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistitem',
            name='content',
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='item',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]