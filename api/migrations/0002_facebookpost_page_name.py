# Generated by Django 3.1.5 on 2021-01-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpost',
            name='page_name',
            field=models.CharField(default='syrianfeminists', max_length=128),
            preserve_default=False,
        ),
    ]
