# Generated by Django 4.2.1 on 2023-08-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=1000)),
                ('age', models.IntegerField(default=0)),
                ('date_enrolled', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
