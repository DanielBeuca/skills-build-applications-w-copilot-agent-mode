from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        teams = [
            {'_id': 1, 'name': 'Team Marvel'},
            {'_id': 2, 'name': 'Team DC'},
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {'_id': 1, 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': 1},
            {'_id': 2, 'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': 1},
            {'_id': 3, 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': 2},
            {'_id': 4, 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': 2},
        ]
        db.users.insert_many(users)
        db.users.create_index('email', unique=True)

        # Activities
        activities = [
            {'user_id': 1, 'activity': 'Running', 'duration': 30},
            {'user_id': 2, 'activity': 'Cycling', 'duration': 45},
            {'user_id': 3, 'activity': 'Swimming', 'duration': 60},
            {'user_id': 4, 'activity': 'Yoga', 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team_id': 1, 'points': 150},
            {'team_id': 2, 'points': 140},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user_id': 1, 'workout': 'Pushups', 'reps': 50},
            {'user_id': 2, 'workout': 'Situps', 'reps': 60},
            {'user_id': 3, 'workout': 'Pullups', 'reps': 20},
            {'user_id': 4, 'workout': 'Squats', 'reps': 80},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
