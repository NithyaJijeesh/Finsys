# Generated by Django 4.1.4 on 2023-05-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0078_remove_retainerinvoices_never_expiring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retainerinvoices',
            name='invoice_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='retainerinvoices',
            name='reference_number',
            field=models.IntegerField(null=True),
        ),
    ]
