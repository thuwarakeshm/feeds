# Generated by Django 2.1.1 on 2018-09-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_alt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]