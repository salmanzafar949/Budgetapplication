# Generated by Django 2.1.7 on 2019-03-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20190319_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_list', to='budget.Project'),
        ),
    ]