# import csv
# from django.core.management.base import BaseCommand
# from states.models import State

# class Command(BaseCommand):
#     # Full path to the CSV file in your Downloads folder
#     csv_file_path = r'C:\Users\Pankaj\Downloads\state.csv'  # Adjust the path if needed

#     def handle(self, *args, **kwargs):
#         with open(self.csv_file_path, 'r') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 title = row['title'].strip()  # Strip spaces to avoid issues with trailing/leading spaces
#                 latitude = row['latitude']
#                 logitude = row['logitude']
#                 pincode = row['pincode']

#                 # Try to match the title exactly as it is in the database
#                 try:
#                     state = State.objects.get(title=title)  # Use exact match (case-sensitive)
#                     state.latitude = latitude
#                     state.logitude = logitude
#                     state.pincode = pincode
#                     state.save()

#                     self.stdout.write(self.style.SUCCESS(f"Successfully updated {title}: Latitude - {latitude}, Longitude - {logitude}, Pincode - {pincode}"))
#                 except State.DoesNotExist:
#                     self.stdout.write(self.style.ERROR(f"State with title '{title}' not found in the database."))
#                 except Exception as e:
#                     self.stdout.write(self.style.ERROR(f"Error updating {title}: {str(e)}"))
import csv
from django.core.management.base import BaseCommand
from states.models import State

class Command(BaseCommand):
    # Full path to the CSV file in your Downloads folder
    csv_file_path = r'C:\Users\Pankaj\Downloads\state.csv'  # Adjust the path if needed

    def handle(self, *args, **kwargs):
        with open(self.csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                title = row['title'].strip()  # Strip spaces to avoid issues with trailing/leading spaces
                latitude = row['latitude']
                logitude = row['logitude']
                pincode = row['pincode']

                # Try to match the title exactly as it is in the database
                try:
                    state = State.objects.get(title=title)  # Use exact match (case-sensitive)
                    state.latitude = latitude
                    state.logitude = logitude
                    state.pincode = pincode
                    state.save()

                    self.stdout.write(self.style.SUCCESS(f"Successfully updated {title}: Latitude - {latitude}, Longitude - {logitude}, Pincode - {pincode}"))
                except State.DoesNotExist:
                    # If state doesn't exist, create a new entry
                    state = State.objects.create(
                        title=title,
                        latitude=latitude,
                        logitude=logitude,
                        pincode=pincode
                    )
                    self.stdout.write(self.style.SUCCESS(f"Successfully created new state entry: {title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error updating {title}: {str(e)}"))
