import random
from tqdm import tqdm
from termcolor import colored
from datetime import datetime, timedelta
from prettytable import PrettyTable

class SlideAssignmentManager:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name):
        self.tables[table_name] = {"assignments": None, "end_date": None}

    def assign_slides(self, slides, people, table_name):
        slides = [int(slide) for slide in slides]
        assignments = {}

        with tqdm(total=len(slides), desc=f"Assigning slides to {table_name}", unit="slide", dynamic_ncols=True) as pbar:
            while slides:
                slide = random.choice(slides)
                person = random.choice(people)

                if person not in assignments:
                    assignments[person] = []

                assignments[person].append(slide)
                slides.remove(slide)
                pbar.update(1)

        self.tables[table_name]["assignments"] = assignments

    def print_assignments(self, table_name):
        assignments = self.tables[table_name]["assignments"]

        if assignments is None:
            print("No assignments found for this table.")
            return

        table = PrettyTable()
        table.field_names = ["Person", "Assigned Slides"]

        for person, slides in assignments.items():
            table.add_row([colored(person, 'blue'), colored(slides, 'yellow')])

        print(colored(f"Assigned slides for {table_name}:", "green"))
        print(table)

    def print_additional_info(self, table_name):
        assignments = self.tables[table_name]["assignments"]

        if assignments is None:
            print("No assignments found for this table.")
            return

        total_assigned = sum(len(slides) for slides in assignments.values())
        print(f"\nTotal slides assigned for {table_name}: {colored(total_assigned, 'cyan')}")

        max_assigned_person = max(assignments, key=lambda person: len(assignments[person]))
        max_assigned_slides = len(assignments[max_assigned_person])
        print(f"Person with the most assigned slides: {colored(max_assigned_person, 'blue')} "
              f"({colored(max_assigned_slides, 'cyan')} slides)")

    def show_days_left(self, table_name):
        end_date = self.tables[table_name]["end_date"]

        if end_date is None:
            print("No end date found for this table.")
            return

        today = datetime.now()
        days_left = (end_date - today).days

        print(f"\nLast Date for {table_name}: {colored(end_date.strftime('%Y-%m-%d'), 'magenta')}")
        print(f"Days Left: {colored(days_left, 'magenta')} days")

    def export_to_csv(self, table_name):
        assignments = self.tables[table_name]["assignments"]

        if assignments is None:
            print("No assignments found for this table.")
            return

        import csv

        with open(f'{table_name}_assignments.csv', 'w', newline='') as csvfile:
            fieldnames = ['Person', 'Assigned Slides']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for person, slides in assignments.items():
                writer.writerow({'Person': person, 'Assigned Slides': ', '.join(map(str, slides))})

        print(f"Data exported to '{table_name}_assignments.csv'")

    def interactive_menu(self):
        while True:
            print("\nInteractive Menu:")
            print("1. Create Table")
            print("2. Assign Slides")
            print("3. Show Assignments")
            print("4. Additional Information")
            print("5. Show Days Left")
            print("6. Export to CSV")
            print("7. Switch Table")
            print("8. Quit")

            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                table_name = input("Enter a name for the new table: ")
                self.create_table(table_name)
                print(f"Table '{table_name}' created.")
            elif choice == '2':
                table_name = input("Enter the name of the table to assign slides: ")
                slides_input = input("Enter the assigning work names or numbers, separated by commas: ").split(",")
                people_input = input("Enter the people's names, separated by commas: ").split(",")
                self.assign_slides(slides_input, people_input, table_name)
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '3':
                table_name = input("Enter the name of the table to show assignments: ")
                self.print_assignments(table_name)
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '4':
                table_name = input("Enter the name of the table to show additional information: ")
                self.print_additional_info(table_name)
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '5':
                table_name = input("Enter the name of the table to show days left: ")
                self.show_days_left(table_name)
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '6':
                table_name = input("Enter the name of the table to export to CSV: ")
                self.export_to_csv(table_name)
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '7':
                table_name = input("Enter the name of the table to switch to: ")
                if table_name in self.tables:
                    print(f"Switched to table '{table_name}'.")
                else:
                    print(f"Table '{table_name}' not found.")
                back_to_menu = input("Press Enter to go back to the menu.")
            elif choice == '8':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    manager = SlideAssignmentManager()
    manager.interactive_menu()
