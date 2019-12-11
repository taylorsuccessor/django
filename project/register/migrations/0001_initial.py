# Generated by Django 2.1 on 2019-09-04 16:57

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('experience_years', models.IntegerField(default=5)),
                ('department_id', models.CharField(blank=True, choices=[('IT', 'IT'), ('HR', 'HR'), ('FINANCE', 'FINANCE')], max_length=7, null=True)),
                ('resume', models.FileField(upload_to=register.models.get_upload_path)),
            ],
        ),
    ]