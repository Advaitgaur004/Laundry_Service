# Generated by Django 4.2 on 2023-05-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clothselection", "0003_cloth_selection_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cloth_selection",
            name="profile_image",
        ),
    ]