# Generated by Django 2.2.4 on 2019-09-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=128),
        ),
    ]
