# Generated by Django 3.2.3 on 2021-07-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('href', models.CharField(max_length=100)),
                ('create_data', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='public_data',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
