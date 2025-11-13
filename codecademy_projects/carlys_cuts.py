hairstyles = [
    "bouffant",
    "pixie",
    "dreadlocks",
    "crew",
    "bowl",
    "bob",
    "mohawk",
    "flattop",
]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# my code starts

total_price = 0

# calculates the total price of every haircut
for price in prices:
    total_price += price

# generates and prints rounded average using "total_price" and dividing by length of "prices"
average_price = total_price / len(prices)
print("Average Haircut Price:", round(average_price, 2))

# generates new prices
new_prices = [i - 5 for i in prices]
print(new_prices)

total_revenue = 0

# multiplies each corresponding index of "prices" and "last_week" and adds them together
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

# takes average of "total_revenue" using the length of "last_week"
average_daily_revenue = total_revenue / len(last_week)
print("Average Daily Revenue:", round(average_daily_revenue, 2))

# creats new list of hairstyles under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
