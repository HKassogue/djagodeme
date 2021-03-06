# Generated by Django 3.2 on 2021-06-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djago', '0006_alter_projet_date_pub'),
        ('deme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='don',
            name='projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='djago.projet'),
        ),
        migrations.AddField(
            model_name='don',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='djago.utilisateur'),
        ),
        migrations.AddField(
            model_name='financement',
            name='projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='djago.projet'),
        ),
        migrations.AddField(
            model_name='financement',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='djago.utilisateur'),
        ),
        migrations.AddField(
            model_name='versement',
            name='destination',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Versements_reçus', to='djago.compte', verbose_name='destination'),
        ),
        migrations.AddField(
            model_name='versement',
            name='don',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='deme.don'),
        ),
        migrations.AddField(
            model_name='versement',
            name='financement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='deme.financement'),
        ),
        migrations.AddField(
            model_name='versement',
            name='source',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Versements_effectués', to='djago.compte', verbose_name='source'),
        ),
    ]
