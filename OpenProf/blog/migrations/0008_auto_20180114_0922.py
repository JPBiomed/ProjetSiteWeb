# Generated by Django 2.0.1 on 2018-01-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
    ]