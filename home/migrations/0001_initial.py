# Generated by Django 4.0.3 on 2022-03-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('about_img', models.ImageField(upload_to=None)),
                ('about_text', models.TextField()),
            ],
        ),
    ]