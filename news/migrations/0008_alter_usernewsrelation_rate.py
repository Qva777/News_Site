# Generated by Django 4.1.4 on 2022-12-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_category_title_alter_news_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernewsrelation',
            name='rate',
            field=models.PositiveIntegerField(choices=[(1, 'Fine'), (2, 'Not bab'), (3, 'Bad')]),
        ),
    ]