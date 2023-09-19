# Generated by Django 4.1.7 on 2023-02-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField()),
            ],
        ),
    ]
