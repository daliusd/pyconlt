# Generated by Django 2.1.5 on 2019-02-04 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_span', models.IntegerField(choices=[(1, 'Single track'), (2, 'All tracks')], help_text='Does the slot span one track or all tracks (like keynote talks and breaks)')),
                ('name', models.CharField(blank=True, help_text="The name of the slot. Only necessary if it's a generic slot and no talks are asigned to it. If a slot is associated with a talk, a talk info will be shown", max_length=255, null=True)),
                ('start_time', models.DateTimeField(help_text='The start time of the slot')),
                ('length', models.IntegerField(help_text='Length of the slot in minutes')),
                ('parent_slot', models.ForeignKey(blank=True, help_text='A slot can be nested inside another slot. If this is the case, connect it here', null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.Slot')),
                ('talk', models.OneToOneField(blank=True, help_text="If it's a slot for a talk, select your talk here.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='proposals.Proposal')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name of a track.', max_length=255)),
                ('room', models.CharField(blank=True, help_text='In which room the track will take place.', max_length=255, null=True)),
                ('moderator', models.CharField(blank=True, help_text='Who will be a moderator of this track.', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='track',
            field=models.ForeignKey(blank=True, help_text='The track to which the slot belongs', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='program.Track'),
        ),
    ]
