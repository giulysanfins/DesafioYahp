# Generated by Django 3.1.1 on 2020-09-03 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("func", "0011_auto_20200903_2001"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transacao",
            name="imagem",
            field=models.ImageField(default="images/default.jpg", upload_to="images"),
        ),
    ]
