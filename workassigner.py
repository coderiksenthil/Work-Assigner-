"""i am using random libarary which i am making while learning it and you are welcome to
modify this code.
"""
import random
slides = input("Enter the assigning work names or numbers, separated by commas: ").split(",")
people = input("Enter the people's names, separated by commas: ").split(",")
# this code is for the list of the slide numbers
slides = [int(slide) for slide in slides]
# this is a empty set for the dictionary to store the assigned slides for each person
assignments = {}
# Randomly assign each slide to a person
while slides:
    slide = random.choice(slides)
    person = random.choice(people)

    if person not in assignments:
        assignments[person] = []

    assignments[person].append(slide)
    slides.remove(slide)
# after all you will get assigned slides for each person
for person, slides in assignments.items():
    print(f"{person}: {slides}")