# Generated by Django 4.1 on 2023-05-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0083_recurring_expense_profile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_expense',
            name='file',
            field=models.FileField(default='default.png', upload_to='purchase/recurring_expense'),
        ),
    ]
