# Generated by Django 2.1 on 2019-01-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min_doc', '0002_auto_20190102_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=32, verbose_name='Status'),
        ),
    ]
