# Generated by Django 4.1.4 on 2023-05-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0080_retainerinvoiceitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='retainerinvoices',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
