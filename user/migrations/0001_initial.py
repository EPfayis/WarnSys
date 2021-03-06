# Generated by Django 4.0.4 on 2022-04-17 04:36

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations, models
import django.db.models.deletion
from user.models import User


def createSuperUser():

    obj_user = User()
    obj_user.is_superuser = True
    obj_user.first_name = "admin"
    obj_user.username = "admin"
    obj_user.email = ""
    obj_user.password = make_password("123123")
    obj_user.save()
    print("admin account created")

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TblUserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.TextField()),
                ('email', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(createSuperUser),
    ]
