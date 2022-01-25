# Generated by Django 3.2.8 on 2021-10-10 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0002_resume_contry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='Contry',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Phone',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]