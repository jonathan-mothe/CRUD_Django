# Generated by Django 3.2 on 2021-04-30 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_inclusion',
            field=models.DateTimeField(),
        ),
    ]
