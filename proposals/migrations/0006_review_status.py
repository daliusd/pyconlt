# Generated by Django 2.1.7 on 2019-03-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0005_auto_20190328_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0, verbose_name='Status'),
        ),
    ]
