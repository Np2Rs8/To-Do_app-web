# Generated by Django 4.1.3 on 2022-12-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(blank=True, max_length=254, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('cuerpo', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Task_list',
                'verbose_name_plural': 'Tasks_lists',
                'ordering': ['timestamp'],
            },
        ),
    ]