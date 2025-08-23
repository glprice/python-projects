# shipping details
weight = float(input("Enter the package weight in lbs: "))

# types of shipping and flat charge
ground_shipping = 20.00
ground_shipping_premium = 125.00
drone_shipping = 0.00

# checks for an invalid weight 
if weight <= 0:
  print("ERROR: INVALID WEIGHT")
else:

# prints package details
  print("Package weight:", weight, "lbs\n")

# calculates the cost of shipping for ground shipping and drone shippng
  if weight <= 2:
    ground_shipping += 1.5 * weight
    drone_shipping += 4.5 * weight
  elif weight <= 6:
    ground_shipping += 3.5 * weight
    drone_shipping += 9.0 * weight
  elif weight <=10:
    ground_shipping += 4 * weight
    drone_shipping += 12.0 * weight
  elif weight > 10: 
    ground_shipping += 4.75 * weight
    drone_shipping += 14.25* weight
  else:
    print("Against all odds, you've managed to break my code!!!")
# prints prices for the customer
  print(f"Ground Shipping: ${ground_shipping:.2f}")
  print("Ground Shipping Premium: $125.00")
  print(f"Drone Shipping: ${drone_shipping:.2f}\n")

# determines the cheapest option and prints it
  if ground_shipping < drone_shipping and  ground_shipping < ground_shipping_premium:
    print("Cheapest option: Ground Shipping")
  elif drone_shipping < ground_shipping and drone_shipping < ground_shipping_premium:
    print("Cheapest option: Drone Shipping")
  elif ground_shipping_premium < ground_shipping and ground_shipping_premium < drone_shipping:
    print("Cheapest option: Ground Shipping Premium")
  else:
    print("Please review pricing")