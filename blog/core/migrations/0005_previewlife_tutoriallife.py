# Generated by Django 2.0.7 on 2018-07-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tutorial_id_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
                ('resume', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('pushised_data', models.DateTimeField(blank=True, null=True)),
                ('id_publish', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TutorialLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publish', models.IntegerField()),
                ('author', models.CharField(max_length=250)),
                ('resume', models.TextField()),
                ('title', models.CharField(max_length=250)),
                ('pushised_data', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]