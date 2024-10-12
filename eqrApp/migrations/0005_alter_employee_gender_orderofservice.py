# Generated by Django 4.0.3 on 2024-05-14 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eqrApp', '0004_employee_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Ar-Condicionado', 'Ar-Condicionado'), ('Ventilador', 'Ventilador'), ('Cadeira', 'Acadeira'), ('Patrimonio', 'Patrimonio')], default='Patrimonio', max_length=50),
        ),
        migrations.CreateModel(
            name='OrderOfService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('details', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eqrApp.employee')),
            ],
        ),
    ]
