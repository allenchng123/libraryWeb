# Generated by Django 2.2.4 on 2019-08-18 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='userId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.User'),
        ),
    ]
