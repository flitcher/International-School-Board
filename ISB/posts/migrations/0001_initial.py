# Generated by Django 2.2.10 on 2020-02-12 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('userid', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('userid', models.CharField(max_length=100, null=True)),
                ('postid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Post')),
            ],
        ),
    ]