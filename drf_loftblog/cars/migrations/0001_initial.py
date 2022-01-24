# Generated by Django 4.0.1 on 2022-01-24 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Вин')),
                ('color', models.CharField(max_length=64, verbose_name='Цвет')),
                ('brand', models.CharField(max_length=64, verbose_name='Brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэтчбэк'), (3, 'Универсал'), (4, 'Купе')], verbose_name='Car_Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]