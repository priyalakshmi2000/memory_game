# Generated by Django 4.2.1 on 2023-06-25 14:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memorygame', '0003_games_score_remove_scores_user_delete_game_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Score',
            new_name='Scores',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
