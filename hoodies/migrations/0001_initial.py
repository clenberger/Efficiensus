# Generated by Django 2.2.6 on 2020-03-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hoodie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoodie_brand', models.CharField(max_length=75)),
                ('hoodie_owner', models.CharField(max_length=75)),
                ('description', models.TextField(help_text='Write the desciption of your hoodie!')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]