# Generated by Django 3.2.8 on 2021-10-08 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_susupicious'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='susupicious',
            new_name='suspicious',
        ),
    ]
