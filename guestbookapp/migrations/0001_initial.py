# Generated by Django 2.2.1 on 2019-05-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('pub_person', models.CharField(max_length=5)),
                ('pub_date', models.DateField(verbose_name='date published')),
            ],
        ),
    ]