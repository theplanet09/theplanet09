# Generated by Django 4.0.2 on 2022-02-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_item', models.CharField(max_length=100)),
                ('its_type', models.CharField(max_length=20)),
            ],
        ),
    ]
