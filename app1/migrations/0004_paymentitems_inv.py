# Generated by Django 4.0.6 on 2022-10-31 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_cust_statment_inv_alter_cust_statment_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentitems',
            name='inv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.invoice'),
        ),
    ]
