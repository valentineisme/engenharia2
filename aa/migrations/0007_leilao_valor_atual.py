# Generated by Django 2.2.5 on 2019-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aa', '0006_leilao'),
    ]

    operations = [
        migrations.AddField(
            model_name='leilao',
            name='valor_atual',
            field=models.CharField(max_length=128, null=True),
        ),
    ]