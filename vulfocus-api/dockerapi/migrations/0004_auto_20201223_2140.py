# Generated by Django 2.2.10 on 2020-12-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0003_auto_20201223_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='image_port',
            field=models.CharField(max_length=256, null=True, verbose_name='暴露端口'),
        ),
    ]
