# Generated by Django 4.2.5 on 2023-10-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_site', '0006_alter_category_name_alter_recipe_cooking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(verbose_name='Время приготовления, мин'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=models.CharField(max_length=300, verbose_name='Этапы приготовления'),
        ),
    ]
