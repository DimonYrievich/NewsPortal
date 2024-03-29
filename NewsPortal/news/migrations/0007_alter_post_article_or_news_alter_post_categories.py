# Generated by Django 4.1.2 on 2023-03-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_category_connection_postcategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_or_news',
            field=models.CharField(choices=[('art', 'Статья'), ('new', 'Новость')], default='new', max_length=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='post', through='news.PostCategory', to='news.category'),
        ),
    ]
