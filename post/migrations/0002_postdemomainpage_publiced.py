# Generated by Django 4.2.3 on 2023-07-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdemomainpage',
            name='publiced',
            field=models.BooleanField(default=False),
        ),
    ]
