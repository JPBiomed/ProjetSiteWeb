# Generated by Django 2.0.1 on 2018-01-13 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=254)),
                ('contenu', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('articleRef', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Article')),
            ],
        ),
    ]
