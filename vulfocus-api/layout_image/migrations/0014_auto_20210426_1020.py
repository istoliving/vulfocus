# Generated by Django 2.2.13 on 2021-04-26 10:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layout_image', '0013_auto_20201223_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='layout_id',
            field=models.UUIDField(default=uuid.UUID('2358a3c5-8de4-4ca1-b1fe-815f46fc9155'), editable=False, primary_key=True, serialize=False, verbose_name='编排UUID'),
        ),
        migrations.AlterField(
            model_name='layoutdata',
            name='layout_user_id',
            field=models.UUIDField(default=uuid.UUID('5515c0e0-b103-4cdd-92f2-d715bc083004'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='service_id',
            field=models.UUIDField(default=uuid.UUID('85e00eb2-fc6e-45ff-946f-f7b7c29c3ddc'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainer',
            name='service_container_id',
            field=models.UUIDField(default=uuid.UUID('f37571ce-3d14-4ebd-b327-ee1720f0901e'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainerscore',
            name='layout_service_container_score_id',
            field=models.UUIDField(default=uuid.UUID('438daa13-f346-40a6-8b4e-ea8ab39cacd1'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicenetwork',
            name='layout_service_network_id',
            field=models.UUIDField(default=uuid.UUID('a0db3185-9749-42f1-ac99-47e32857d990'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]