# Generated by Django 5.1.4 on 2025-01-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(db_column='user_name', max_length=50, unique=True)),
                ('user_pass', models.CharField(db_column='user_pass', max_length=100)),
                ('user_email', models.EmailField(db_column='user_email', max_length=254, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time')),
                ('modify_time', models.DateTimeField(blank=True, db_column='modify_time', null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
    ]
