# Generated by Django 3.1.7 on 2021-10-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0097_auto_20210819_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='estimated_hours',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
