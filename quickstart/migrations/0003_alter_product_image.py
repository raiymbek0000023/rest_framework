# Generated by Django 4.1.7 on 2023-03-19 20:31

from django.db import migrations, models
import quickstart.models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_alter_category_options_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=quickstart.models.get_file_path),
        ),
    ]