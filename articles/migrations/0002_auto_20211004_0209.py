# Generated by Django 3.2.7 on 2021-10-03 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Scopeship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематики Статьи',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Scopeship', to='articles.Tag'),
        ),
    ]