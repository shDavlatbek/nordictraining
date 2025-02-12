# Generated by Django 5.1.5 on 2025-01-20 09:05

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contact_news_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_at'], 'verbose_name': 'Murojaat', 'verbose_name_plural': 'Murojaatlar'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('new', 'Yangi'), ('read', "O'qilgan"), ('replied', 'Javob berilgan')], default='new', max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Yoshi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='F.I.O'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='page',
            field=models.CharField(max_length=255, verbose_name='Murojaat-sahifasi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sex',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Jinsi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Kontent'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti"),
        ),
    ]
