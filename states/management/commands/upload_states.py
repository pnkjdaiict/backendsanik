# myapp/management/commands/upload_states.py
import csv
from django.core.management.base import BaseCommand
from states.models import State

class Command(BaseCommand):
    help = 'Load states data from a CSV file'

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\Pankaj\Downloads\states_data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            states = [
                State(
                    title=row['title'],
                   
                )
                for row in reader
            ]
            State.objects.bulk_create(states)
        self.stdout.write(self.style.SUCCESS('States data has been uploaded successfully.'))
