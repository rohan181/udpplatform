# Generated by Django 4.0.1 on 2023-10-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_first_name_user_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(max_length=255, verbose_name='fullname'),
        ),
    ]