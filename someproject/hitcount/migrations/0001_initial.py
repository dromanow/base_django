# Generated by Django 3.2.9 on 2021-11-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('path', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('hits', models.IntegerField(default=1)),
            ],
        ),
    ]