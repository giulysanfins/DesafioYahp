# Generated by Django 3.1.1 on 2020-09-03 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("func", "0015_auto_20200903_2013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transacao",
            name="investimentos",
            field=models.ForeignKey(
                blank=True,
                default="Sem Investimento",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="func.categoria",
            ),
        ),
    ]
