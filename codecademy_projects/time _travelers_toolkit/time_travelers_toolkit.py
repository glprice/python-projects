# importing modules
from custom_module import generate_time_travel_message
import datetime as dt
from decimal import Decimal
import random

# code starts

# current date and time with formatting
current_date = dt.datetime.now()
formatted_dt = current_date.strftime("%B %d, %Y at %I:%M %p")

print(formatted_dt)


# calculating cost
def travel_cost(target_year):
    base_cost = Decimal("3500.00")
    year_difference = abs(dt.datetime.now().year - target_year)
    multiplier = Decimal("10.25")
    cost = base_cost + (multiplier * Decimal(year_difference))

    return round(cost, 2)


# randomizing choice of year and destination
destinations = [
    "Tokyo, Tokyo Prefecture : Japan",
    "Paris, Île-de-France : France",
    "New York City, New York : United States",
    "Sydney, New South Wales : Australia",
    "Toronto, Ontario : Canada",
    "Cape Town, Western Cape : South Africa",
    "São Paulo, São Paulo : Brazil",
    "Berlin, Berlin : Germany",
    "Dubai, Dubai Emirate : United Arab Emirates",
    "Auckland, Auckland Region : New Zealand",
]
random_year = random.randint(1900, 5000)
random_destination = random.choice(destinations)

# generate_time_travel_message with random destination and year
print(
    generate_time_travel_message(
        random_year, random_destination, travel_cost(random_year)
    )
)
