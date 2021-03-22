# Generated by Django 3.1.7 on 2021-03-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('art_data', models.TextField(default=None)),
                ('state', models.DecimalField(decimal_places=0, default=None, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='Articles_tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.IntegerField(default=None)),
                ('id_articles', models.IntegerField(default=None)),
                ('possision', models.DecimalField(decimal_places=0, default=None, max_digits=4)),
                ('url', models.SlugField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('type', models.DecimalField(decimal_places=0, default=None, max_digits=1)),
            ],
        ),
    ]