# Generated by Django 2.1.14 on 2020-02-27 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0049_merge_20200227_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='role',
        ),
    ]
