# Generated by Django 2.0.1 on 2018-01-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180114_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nbrComment',
            field=models.IntegerField(null=True),
        ),
    ]
