# Generated by Django 4.1.5 on 2023-01-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='from_date',
            field=models.DateField(null=True),
        ),
    ]
