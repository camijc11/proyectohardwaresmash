# Generated by Django 4.1.1 on 2022-09-17 17:18

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
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('logo', models.ImageField(upload_to='store/')),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('facebook_url', models.URLField(max_length=250)),
                ('instagram_url', models.URLField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banner/')),
                ('Store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.store')),
            ],
        ),
    ]
