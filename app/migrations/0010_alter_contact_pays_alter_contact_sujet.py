# Generated by Django 4.2.11 on 2024-04-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_contact_pays_alter_contact_sujet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='pays',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sujet',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
