# Generated by Django 2.2.4 on 2019-09-09 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_auto_20190624_1250"),
    ]

    operations = [
        migrations.AlterModelOptions(name="teams", options={"ordering": ("id",)},),
    ]
