# Generated by Django 4.1 on 2023-05-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0082_recurring_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_expense',
            name='profile_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recurring_expense',
            name='repeat_every',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
