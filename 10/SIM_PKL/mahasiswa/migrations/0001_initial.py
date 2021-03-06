# Generated by Django 3.1.2 on 2020-10-15 14:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_auto_20201015_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pkl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('tanggal_mulai', models.DateField(default=datetime.datetime.now)),
                ('tanggal_selesai', models.DateField()),
                ('approve', models.BooleanField(default=False)),
                ('catatan', models.TextField(help_text='maksimal 1500 karakter', max_length=1500)),
                ('reject', models.BooleanField(default=False)),
                ('nama_dosen', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='membimbing', to=settings.AUTH_USER_MODEL)),
                ('nama_mitra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='forum.forum')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mahasiswa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
