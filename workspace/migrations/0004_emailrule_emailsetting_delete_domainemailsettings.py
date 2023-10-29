# Generated by Django 4.2.5 on 2023-10-08 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_emailsettings_domainemailsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.CharField(choices=[('Auto-Reply', 'Auto-Reply'), ('Forward', 'Forward'), ('Spam Filter', 'Spam Filter')], max_length=50)),
                ('condition', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_reply', models.TextField(blank=True, null=True)),
                ('forwarding_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('spam_filter_level', models.IntegerField(default=1)),
                ('signature', models.TextField(blank=True, null=True)),
                ('vacation_mode_start', models.DateField(blank=True, null=True)),
                ('vacation_mode_end', models.DateField(blank=True, null=True)),
                ('vacation_message', models.TextField(blank=True, null=True)),
                ('read_receipt', models.BooleanField(default=False)),
                ('email_priority', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DomainEmailSettings',
        ),
    ]
