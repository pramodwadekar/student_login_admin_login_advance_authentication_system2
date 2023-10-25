# Generated by Django 4.2.6 on 2023-10-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_student_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
