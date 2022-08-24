# Generated by Django 4.1 on 2022-08-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timeAdded', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dapp.topic')),
            ],
            options={
                'verbose_name_plural': 'recordies',
            },
        ),
    ]
