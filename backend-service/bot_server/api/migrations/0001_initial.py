# Generated by Django 3.1 on 2020-09-07 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('log_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'log_department',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('log_course_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dept')),
            ],
            options={
                'db_table': 'log_course',
            },
        ),
    ]