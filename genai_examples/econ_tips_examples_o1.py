"""
Economic Insights Generator
Author: John Doe
Date: October 1, 2023

This script provides personalized economic insights to the user based on random selection and user input.
"""

# Import necessary modules
import random

# Pseudocode:
# 1. Greet the user and ask for their name.
# 2. Strip any leading/trailing whitespace and convert the name to title case.
# 3. Ask the user for their area of interest in economics (e.g., 'inflation', 'GDP', 'unemployment', 'stock market').
# 4. Normalize the input by converting it to lower case and removing extra spaces.
# 5. Check if the input is valid using boolean expressions.
# 6. If valid, randomly select an insight from the chosen category and display it.
# 7. If not valid, inform the user and provide a general economic insight.
# 8. Thank the user.

# Lists of economic insights
inflation_insights = [
    "Inflation reduces the purchasing power of money over time.",
    "Central banks often adjust interest rates to control inflation.",
    "Hyperinflation can lead to a rapid decline in a currency's value."
]

gdp_insights = [
    "GDP measures the total value of goods and services produced in a country.",
    "A rising GDP indicates economic growth.",
    "GDP per capita is a useful indicator of a country's standard of living."
]

unemployment_insights = [
    "High unemployment can lead to decreased consumer spending.",
    "The unemployment rate is a lagging indicator of economic health.",
    "Structural unemployment occurs when workers' skills do not match job requirements."
]

stock_market_insights = [
    "Diversification can reduce investment risk in the stock market.",
    "Stock prices are influenced by company performance and market sentiment.",
    "The stock market is often considered a leading indicator of economic trends."
]

general_insights = inflation_insights + gdp_insights + unemployment_insights + stock_market_insights

# 1. Greet the user and ask for their name.
print("Welcome to the Economic Insights Generator!")

user_name = input("Please enter your name: ")

# 2. Strip any leading/trailing whitespace and convert the name to title case.
user_name = user_name.strip().title()

# 3. Ask the user for their area of interest.
print(f"Hello, {user_name}!")
interest_area = input("Which economic topic are you interested in? (Inflation/GDP/Unemployment/Stock Market): ")

# 4. Normalize the input.
interest_area = interest_area.strip().lower()
interest_area_normalized = interest_area.replace(" ", "").replace("-", "")

# 5. Check if the input is valid using boolean expressions.
if not interest_area_normalized:
    print("You did not enter a topic. Here is a general economic insight:")
    insight = random.choice(general_insights)
elif interest_area_normalized == 'inflation' or 'inflation' in interest_area_normalized:
    insight = random.choice(inflation_insights)
elif interest_area_normalized == 'gdp' or 'grossdomesticproduct' in interest_area_normalized:
    insight = random.choice(gdp_insights)
elif interest_area_normalized == 'unemployment' or 'joblessness' in interest_area_normalized:
    insight = random.choice(unemployment_insights)
elif interest_area_normalized == 'stockmarket' or 'stocks' in interest_area_normalized or 'market' in interest_area_normalized:
    insight = random.choice(stock_market_insights)
else:
    # 7. If not valid, inform the user and provide a general insight.
    print("Sorry, we didn't recognize that topic.")
    insight = random.choice(general_insights)

# 6. Display the selected economic insight.
print("\nHere is your economic insight:")
print(insight)

# 8. Thank the user.
print(f"\nThank you for using the Economic Insights Generator, {user_name}!")

# Notes:
# - random.choice() is a function that selects a random element from a list.
# - strip(), lower(), replace(), and title() are string methods that modify string objects.
# - We used boolean expressions with 'and', 'or', and 'not' to validate user input.
# - The 'in' keyword checks for membership in strings and lists.