# Generated by Django 2.2 on 2019-09-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0004_auto_20190907_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.AddField(
            model_name='event',
            name='categories',
            field=models.ManyToManyField(related_name='events', to='eventFinderApp.Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=200),
        ),
    ]
