# Generated by Django 4.2.1 on 2023-06-06 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zzp', '0009_remove_korisnik_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kviz',
            name='idorg',
            field=models.ForeignKey(db_column='idOrg', on_delete=django.db.models.deletion.CASCADE, to='zzp.organizator'),
        ),
        migrations.AlterField(
            model_name='organizator',
            name='predstojecikviz',
            field=models.ForeignKey(db_column='predstojeciKviz', null=True, on_delete=django.db.models.deletion.CASCADE, to='zzp.kviz'),
        ),
        migrations.AlterField(
            model_name='prijava',
            name='idkor',
            field=models.ForeignKey(db_column='idKor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prijava',
            name='idkviz',
            field=models.ForeignKey(db_column='idKviz', on_delete=django.db.models.deletion.CASCADE, to='zzp.kviz'),
        ),
        migrations.AlterField(
            model_name='recenzija',
            name='idkorrec',
            field=models.ForeignKey(db_column='idKorRec', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recenzija',
            name='idorgrec',
            field=models.ForeignKey(db_column='idOrgRec', on_delete=django.db.models.deletion.CASCADE, to='zzp.organizator'),
        ),
    ]