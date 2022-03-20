# Generated by Django 4.0.3 on 2022-03-20 17:04

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
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_name', models.CharField(choices=[('DON', 'Donholm'), ('PIP', 'Pipeline'), ('BUR', 'Buruburu'), ('DHA', 'Fedha'), ('EMB', 'Embakasi')], default='DON', max_length=3)),
                ('location', models.CharField(max_length=30)),
                ('occupants_count', models.IntegerField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('neighbourhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('business_email', models.EmailField(max_length=254)),
                ('neighbourhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbour.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]