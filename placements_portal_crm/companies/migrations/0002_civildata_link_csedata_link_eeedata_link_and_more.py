# Generated by Django 4.1.4 on 2022-12-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='civildata',
            name='link',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='csedata',
            name='link',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='eeedata',
            name='link',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='mechdata',
            name='link',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]