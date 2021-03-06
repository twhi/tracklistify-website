# Generated by Django 2.2.5 on 2020-02-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('show_url', models.CharField(max_length=1000)),
                ('tracks_found', models.IntegerField(default=0)),
                ('total_tracks', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
