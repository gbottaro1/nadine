# Generated by Django 3.0.4 on 2020-04-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nadine', '0037_userprofile_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='usercode',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]
