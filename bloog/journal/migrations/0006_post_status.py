# Generated by Django 5.1 on 2024-08-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
