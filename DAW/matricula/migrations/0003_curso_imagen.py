# Generated by Django 2.2.5 on 2019-10-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_alumno_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
    ]
