# Generated by Django 4.1.3 on 2022-12-04 03:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
