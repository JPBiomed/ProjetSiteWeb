# Generated by Django 2.0.1 on 2018-01-13 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180113_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='articleRef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Article'),
        ),
    ]