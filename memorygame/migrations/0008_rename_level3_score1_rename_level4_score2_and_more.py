# Generated by Django 4.2.1 on 2023-07-11 14:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memorygame', '0007_level1_level2_level3_level4_delete_scores'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='level3',
            new_name='score1',
        ),
        migrations.RenameModel(
            old_name='level4',
            new_name='score2',
        ),
        migrations.RenameModel(
            old_name='level1',
            new_name='score3',
        ),
        migrations.RenameModel(
            old_name='level2',
            new_name='score4',
        ),
    ]
