# Generated by Django 4.2.1 on 2023-06-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizator',
            name='teme',
            field=models.CharField(max_length=255, null=True),
        ),
    ]