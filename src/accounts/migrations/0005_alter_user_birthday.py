# Generated by Django 3.2.10 on 2023-03-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
