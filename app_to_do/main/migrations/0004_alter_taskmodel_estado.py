# Generated by Django 4.1.3 on 2022-12-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_taskmodel_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='estado',
            field=models.CharField(choices=[(0, 'Incompleto'), (1, 'Proceso'), (2, 'Completado')], default='incompleto', max_length=50),
        ),
    ]