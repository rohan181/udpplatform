# Generated by Django 4.0.1 on 2023-10-22 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_profilecomplete5_profilecomplete4_profilecomplete3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilecomplete1',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
