# Generated by Django 5.1.7 on 2025-04-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promptdata',
            name='isSharable',
            field=models.BooleanField(default=False),
        ),
    ]
