# Generated by Django 4.2.9 on 2024-01-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuApp', '0004_eater'),
    ]

    operations = [
        migrations.AddField(
            model_name='eater',
            name='creator',
            field=models.CharField(default='___________', max_length=255),
            preserve_default=False,
        ),
    ]
