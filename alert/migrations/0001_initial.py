# Generated by Django 4.0.4 on 2022-04-26 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picture.tblimage')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.tblmainlocations')),
            ],
        ),
    ]