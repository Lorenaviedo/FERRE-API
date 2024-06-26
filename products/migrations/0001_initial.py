# Generated by Django 5.0.6 on 2024-06-21 14:29

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
                ('titleProduct', models.CharField(max_length=150)),
                ('imgProduct', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
