# Generated by Django 3.1.1 on 2020-09-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func', '0013_auto_20200903_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='imagem',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images'),
        ),
    ]