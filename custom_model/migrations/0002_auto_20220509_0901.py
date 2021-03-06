# Generated by Django 3.2 on 2022-05-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='description',
            field=models.TextField(default='information about NFT here', max_length=200),
        ),
        migrations.AddField(
            model_name='nft',
            name='rating',
            field=models.IntegerField(default='00', verbose_name=3),
        ),
        migrations.AlterField(
            model_name='nft',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
