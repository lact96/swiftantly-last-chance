# Generated by Django 4.2.5 on 2023-10-07 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_virtualdomain_remove_customuser_imap_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_limit', models.IntegerField(default=100)),
                ('rate_limit_type', models.CharField(choices=[('per_minute', 'Per Minute'), ('per_hour', 'Per Hour')], default='per_minute', max_length=10)),
                ('max_attachment_size', models.IntegerField(default=10240)),
                ('max_recipients', models.IntegerField(default=50)),
                ('spam_filter_level', models.IntegerField(default=1)),
                ('auto_delete_spam', models.BooleanField(default=False)),
                ('auto_archive_duration', models.IntegerField(default=30)),
                ('encryption_type', models.CharField(choices=[('TLS', 'TLS'), ('SSL', 'SSL'), ('None', 'None')], default='TLS', max_length=5)),
                ('authentication_required', models.BooleanField(default=True)),
                ('log_level', models.CharField(choices=[('Error', 'Error'), ('Warning', 'Warning'), ('Info', 'Info'), ('Debug', 'Debug')], default='Info', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DomainEmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_limit', models.IntegerField(default=100)),
                ('rate_limit_type', models.CharField(choices=[('per_minute', 'Per Minute'), ('per_hour', 'Per Hour')], default='per_minute', max_length=10)),
                ('max_attachment_size', models.IntegerField(default=10240)),
                ('max_recipients', models.IntegerField(default=50)),
                ('spam_filter_level', models.IntegerField(default=1)),
                ('auto_delete_spam', models.BooleanField(default=False)),
                ('auto_archive_duration', models.IntegerField(default=30)),
                ('encryption_type', models.CharField(choices=[('TLS', 'TLS'), ('SSL', 'SSL'), ('None', 'None')], default='TLS', max_length=5)),
                ('authentication_required', models.BooleanField(default=True)),
                ('log_level', models.CharField(choices=[('Error', 'Error'), ('Warning', 'Warning'), ('Info', 'Info'), ('Debug', 'Debug')], default='Info', max_length=10)),
                ('domain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workspace.virtualdomain')),
            ],
        ),
    ]
