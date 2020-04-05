# Generated by Django 3.0.4 on 2020-03-31 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0004_auto_20200331_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='created_ts',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 23, 37, 37, 930788)),
        ),
        migrations.AlterField(
            model_name='policy',
            name='type',
            field=models.CharField(choices=[('SIG', 'Signature'), ('WLP', 'Whitelist part'), ('BLP', 'Blacklist part'), ('CGR', 'Control group')], max_length=3),
        ),
        migrations.AlterField(
            model_name='policy',
            name='updated_ts',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 23, 37, 37, 930828)),
        ),
    ]
