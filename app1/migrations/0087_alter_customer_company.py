# Generated by Django 4.1 on 2023-06-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0086_recurring_expense_gstin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]