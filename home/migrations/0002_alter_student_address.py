# Generated by Django 5.0.4 on 2024-04-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]

'''if i dlt '0001_initial' file then our data gets colab because
the migration files also get stored in the django database.'''

