# Generated by Django 5.1 on 2024-08-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=15)),
                ('priority', models.IntegerField(default=10)),
                ('last_update', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
