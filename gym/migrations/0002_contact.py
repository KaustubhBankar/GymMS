# Generated by Django 3.2.4 on 2023-04-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('emailid', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=300, null=True)),
                ('msgdate', models.DateTimeField(auto_now_add=True)),
                ('isread', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
