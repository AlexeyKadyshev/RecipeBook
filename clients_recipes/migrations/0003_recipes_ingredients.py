# Generated by Django 5.0.4 on 2024-05-07 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_recipes', '0002_categories_recipes_user_user_date_add_reciepcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Ингредиенты'),
            preserve_default=False,
        ),
    ]