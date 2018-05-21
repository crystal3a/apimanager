# Generated by Django 2.0.5 on 2018-05-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreyeendetail',
            fields=[
                ('seqid', models.IntegerField(db_column='SeqID', primary_key=True, serialize=False)),
                ('entryno', models.IntegerField(blank=True, db_column='EntryNo', null=True)),
                ('entryword', models.TextField(blank=True, db_column='EntryWord', null=True)),
                ('orgcode', models.TextField(blank=True, db_column='OrgCode', null=True)),
                ('item', models.TextField(blank=True, db_column='Item', null=True)),
                ('groupno', models.TextField(blank=True, db_column='GroupNo', null=True)),
                ('itemcontent', models.TextField(blank=True, db_column='ItemContent', null=True)),
                ('enitem', models.TextField(blank=True, db_column='EnItem', null=True)),
                ('chitem', models.TextField(blank=True, db_column='ChItem', null=True)),
            ],
            options={
                'db_table': 'DreyeENDetail',
            },
        ),
        migrations.CreateModel(
            name='Dreyemainen',
            fields=[
                ('entryno', models.IntegerField(db_column='EntryNo', primary_key=True, serialize=False)),
                ('entryword', models.TextField(blank=True, db_column='EntryWord', null=True)),
                ('kksymbol', models.TextField(blank=True, db_column='KKsymbol', null=True)),
                ('djsymbol', models.TextField(blank=True, db_column='DJsymbol', null=True)),
                ('online', models.TextField(blank=True, db_column='Online', null=True)),
                ('modifydatetime', models.DateTimeField(db_column='ModifyDateTime')),
            ],
            options={
                'db_table': 'DreyeMainEN',
            },
        ),
    ]
