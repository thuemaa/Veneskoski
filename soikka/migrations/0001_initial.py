# Generated by Django 2.0.7 on 2018-07-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajankohtaista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otsikko', models.CharField(max_length=200)),
                ('teksti', models.TextField()),
            ],
        ),
    ]
