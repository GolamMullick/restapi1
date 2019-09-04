# Generated by Django 2.1.2 on 2019-09-04 08:57

from django.db import migrations, models
import django.db.models.deletion
import restapi1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('maxstudent', models.IntegerField(default=100)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(default=restapi1.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi1.Student'),
        ),
    ]