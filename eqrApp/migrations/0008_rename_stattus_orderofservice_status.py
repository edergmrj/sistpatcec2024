# Generated by Django 4.0.3 on 2024-05-20 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eqrApp', '0007_alter_orderofservice_stattus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderofservice',
            old_name='stattus',
            new_name='status',
        ),
    ]
