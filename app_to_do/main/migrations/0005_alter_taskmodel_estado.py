# Generated by Django 4.1.3 on 2022-12-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_taskmodel_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='estado',
            field=models.CharField(default='incompleto', max_length=50),
        ),
    ]
