"""
Health Tips Generator
Author: Jane Smith
Date: October 1, 2023

This script provides personalized health tips to the user based on random selection and user input.
"""

# Import necessary modules
import random

# Pseudocode:
# 1. Greet the user and ask for their name.
# 2. Strip any leading/trailing whitespace and convert the name to title case.
# 3. Ask the user for their preferred type of health tip (e.g., 'nutrition', 'exercise', 'mental health').
# 4. Normalize the input by converting it to lower case and removing extra spaces.
# 5. Check if the input is valid using boolean expressions.
# 6. If valid, randomly select a tip from the chosen category and display it.
# 7. If not valid, inform the user and provide a random tip from any category.
# 8. Thank the user.

# Lists of health tips
nutrition_tips = [
    "Eat a variety of foods for a balanced diet.",
    "Include plenty of fruits and vegetables in your meals.",
    "Stay hydrated by drinking enough water."
]

exercise_tips = [
    "Aim for at least 30 minutes of moderate exercise daily.",
    "Incorporate strength training exercises twice a week.",
    "Take the stairs instead of the elevator."
]

mental_health_tips = [
    "Practice mindfulness and meditation.",
    "Ensure you get enough sleep each night.",
    "Stay connected with friends and family."
]

all_tips = nutrition_tips + exercise_tips + mental_health_tips

# 1. Greet the user and ask for their name.
print("Welcome to the Health Tips Generator!")

name = input("Please enter your name: ")

# 2. Strip any leading/trailing whitespace and convert the name to title case.
name = name.strip().title()

# 3. Ask the user for their preferred type of health tip.
print(f"Hello, {name}!")
tip_category = input("Which type of health tip would you like? (Nutrition/Exercise/Mental Health): ")

# 4. Normalize the input.
tip_category = tip_category.strip().lower()
tip_category_normalized = tip_category.replace(" ", "").replace("-", "")

# 5. Check if the input is valid using boolean expressions.
if not tip_category_normalized:
    print("You did not enter a category. Here is a random health tip:")
    tip = random.choice(all_tips)
elif tip_category_normalized == 'nutrition' or tip_category_normalized == 'diet' or 'food' in tip_category_normalized:
    tip = random.choice(nutrition_tips)
elif tip_category_normalized == 'exercise' or tip_category_normalized == 'fitness' or 'sport' in tip_category_normalized:
    tip = random.choice(exercise_tips)
elif ('mental' in tip_category_normalized and 'health' in tip_category_normalized) or 'mind' in tip_category_normalized:
    tip = random.choice(mental_health_tips)
elif 'health' in tip_category_normalized:
    tip = random.choice(all_tips)
else:
    # 7. If not valid, inform the user and provide a random tip from any category.
    print("Sorry, we didn't recognize that category.")
    tip = random.choice(all_tips)

# 6. Display the selected health tip.
print("\nHere is your health tip:")
print(tip)

# 8. Thank the user.
print(f"\nThank you for using the Health Tips Generator, {name}!")

# Notes:
# - random.choice() is a function that selects a random element from a list.
# - strip(), lower(), replace(), and title() are string methods that act on string objects.
# - We used boolean expressions with 'and', 'or', and 'not' to validate user input.
# - The 'in' keyword checks for membership in strings and lists.