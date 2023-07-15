# Generated by Django 4.2.3 on 2023-07-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeaderImage', models.TextField(blank=True, default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F001%2F233%2F908%2Fsmall%2Fmodern-green-overlapping-banner-background.jpg&f=1&nofb=1&ipt=abfd64362b89d2ed7bb0e967e58ebaf5af9df470013d3d3dc64c6f59d22e40f0&ipo=images', null=True)),
                ('ProfileImage', models.TextField(blank=True, default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fblog.alliedmarketresearch.com%2Fimages%2Fuser_icon.png&f=1&nofb=1&ipt=3fa3cccc7873c89c86816feb407f17445fa976943c10f7aff541d36e3ea21bc3&ipo=images', null=True)),
                ('Name', models.CharField(blank=True, max_length=150, null=True)),
                ('AboutMe', models.CharField(blank=True, max_length=450, null=True)),
                ('github', models.CharField(blank=True, max_length=450, null=True)),
                ('twitter', models.CharField(blank=True, max_length=450, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=450, null=True)),
                ('insta', models.CharField(blank=True, max_length=450, null=True)),
            ],
        ),
    ]