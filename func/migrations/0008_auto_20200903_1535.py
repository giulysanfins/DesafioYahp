# Generated by Django 3.1.1 on 2020-09-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("func", "0007_auto_20200903_1513"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transacao",
            old_name="image",
            new_name="imagem",
        ),
    ]
