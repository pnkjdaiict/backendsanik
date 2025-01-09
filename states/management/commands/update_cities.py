import csv
from django.core.management.base import BaseCommand
from states.models import State, Cities  # Assuming you have a City model that links to the State model

class Command(BaseCommand):
    # Full path to the CSV file for cities
    csv_file_path = r'C:\Users\Pankaj\Downloads\city.csv'  # Adjust the path if needed

    def handle(self, *args, **kwargs):
        # Open and read the CSV file
        with open(self.csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                title = row['title'].strip()  # Ensure no leading/trailing spaces
                # If the 'state' field is not in your CSV, you can define it manually or leave it blank
                state = row['state'].strip()  # Assuming the state value is in the CSV row
                latitude = row['latitude']
                logitude = row['logitude']
                pincode = row['pincode']

                try:
                    # Instead of looking up the state by title, we can directly assign the state
                    # Look up the state by its title (exact match)
                    state_instance = State.objects.get(title=state)

                    # Check if the city exists in the database or create it
                    city, created = Cities.objects.get_or_create(
                        title=title, state=state_instance
                    )

                    # Update latitude, longitude, and pincode if they exist
                    city.latitude = latitude
                    city.logitude = logitude
                    city.pincode = pincode
                    city.save()

                    self.stdout.write(self.style.SUCCESS(f"Successfully updated {title}: Latitude - {latitude}, Longitude - {logitude}, Pincode - {pincode}, State - {state_instance.title}"))

                except State.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"State with title '{state}' not found in the database for city '{title}'"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error updating {title}: {str(e)}"))
