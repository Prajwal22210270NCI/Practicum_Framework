# Generated by Django 4.2.7 on 2023-11-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Cement', 'Cement'), ('Bricks', 'Bricks'), ('Tools', 'Tools'), ('Paint', 'Paint')], max_length=50, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
