# Generated by Django 2.0.2 on 2018-02-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180213_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
