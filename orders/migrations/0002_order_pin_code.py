# Generated by Django 5.0.4 on 2024-04-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="pin_code",
            field=models.IntegerField(default=110001),
            preserve_default=False,
        ),
    ]
