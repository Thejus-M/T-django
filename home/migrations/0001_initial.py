# Generated by Django 4.1.7 on 2023-03-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_pic', models.ImageField(upload_to='images')),
                ('description', models.TextField(max_length=1000)),
                ('read_more_url', models.URLField()),
                ('website_url', models.URLField()),
                ('tag', models.ManyToManyField(to='home.tag')),
            ],
        ),
    ]
