# # # import csv
# # # from django.core.management.base import BaseCommand
# # # from states.models import *

# # # class Command(BaseCommand):
# # #     help = 'Load cities data from a CSV file'

# # #     def handle(self, *args, **kwargs):
# # #         # Open the CSV file
# # #         with open(r'C:\Users\Pankaj\Downloads\cities_r2.csv', newline='') as csvfile:
# # #             reader = csv.DictReader(csvfile)
# # #             cities = []
# # #             for row in reader:
# # #                 # Retrieve the associated state by name, case-insensitive match
# # #                 state = State.objects.filter(title__iexact=row['State']).first()
                
# # #                 # if state:
# # #                     # Create a new city for each row
# # #                     # city = Cities(
# # #                     #     title=row['Title'],  # assuming field is 'title' in the Cities model
# # #                     #     state=state,
# # #                     # )
# # #                 cities.append( Cities(
# # #                         title=row['Title'],  # assuming field is 'title' in the Cities model
# # #                         state=state)) 

# # #             # Bulk create all city entries at once
# # #             Cities.objects.bulk_create(cities)
        
# # #         self.stdout.write(self.style.SUCCESS('Cities data has been uploaded successfully.'))
# # from django.core.management.base import BaseCommand
# # from django.db import IntegrityError
# # from states.models import Cities
# # from django.db.models import Count

# # class Command(BaseCommand):
# #     help = 'Remove duplicate cities safely without violating database integrity'

# #     def handle(self, *args, **kwargs):
# #         # Step 1: Find duplicates by state and title (city name)
# #         duplicates = Cities.objects.values('state', 'title').annotate(count=Count('id')).filter(count__gt=1)

# #         for duplicate in duplicates:
# #             state = duplicate['state']
# #             title = duplicate['title']

# #             try:
# #                 # Step 2: Get all cities that match the state and title
# #                 cities_to_delete = Cities.objects.filter(state=state, title=title)
                
# #                 # Keep the first city and delete the rest
# #                 first_city = cities_to_delete.first()
# #                 cities_to_delete.exclude(id=first_city.id).delete()

# #                 self.stdout.write(self.style.SUCCESS(f"Deleted duplicates for city '{title}' in state '{state}'"))
# #             except IntegrityError as e:
# #                 self.stdout.write(self.style.ERROR(f"IntegrityError encountered while deleting duplicates for city '{title}' in state '{state}': {e}"))

# #         self.stdout.write(self.style.SUCCESS('Duplicate cities have been removed successfully.'))
# import csv
# from django.core.management.base import BaseCommand
# from states.models import Cities, State

# class Command(BaseCommand):
#     help = 'Load cities data from a CSV file'

#     def handle(self, *args, **kwargs):
#         # Path to your CSV file
#         csv_file_path = r'C:\Users\Pankaj\Downloads\cities_r2.csv'

#         # Open and read the CSV file
#         with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             cities_to_create = []
#             for row in reader:
#                 city_title = row['Title'].strip()
#                 state_name = row['State'].strip()

#                 # Try to get the corresponding state, case insensitive
#                 state = State.objects.filter(title__iexact=state_name).first()

#                 if state:
#                     # If state exists, create the city
#                     city = Cities(
#                         title=city_title,
#                         state=state,
#                     )
#                     cities_to_create.append(city)
#                 else:
#                     # If the state does not exist, log a warning
#                     self.stdout.write(self.style.WARNING(f"State '{state_name}' not found for city '{city_title}'"))

#             # Bulk create cities
#             Cities.objects.bulk_create(cities_to_create)

#         self.stdout.write(self.style.SUCCESS('Cities data has been uploaded successfully.'))

