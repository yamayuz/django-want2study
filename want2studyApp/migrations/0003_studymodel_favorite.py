# Generated by Django 4.0.2 on 2022-02-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want2studyApp', '0002_studymodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymodel',
            name='favorite',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
