from decimal import Decimal
from datetime import datetime

# ===== Menu Class =====
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time =  datetime.strptime(start_time, "%I:%M %p").time()
    self.end_time = datetime.strptime(end_time, "%I:%M %p").time()

  def __repr__(self):
    return f"{self.name}: {self.start_time} - {self.end_time}"
  
  def calculate_bill(self, purchased_items):
    total = Decimal("0.00")
    for item in purchased_items:
      if item in self.items:
        total += Decimal(str(self.items[item]))
    return total

# ===== Franchise Class =====
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"{self.address}"
  
  def available_menus(self, time):
    items = {}
    name = ""
    kids_items = {}
    kids_menu = False
    adult_menu = False
    
    dt = datetime.strptime(time, "%I:%M %p").time()
    
    def formatting(name, items):
      formatted = f"{name} Menu:\n"
      for item, price in items.items():
          formatted += f"{item}: ${price:.2f}\n"
      return formatted

    for menu in self.menus:
      if dt >= menu.start_time and dt < menu.end_time:
        if menu == kids:
          kids_items.update(menu.items)
          kids_menu = True
        else:
          items.update(menu.items)
          name = menu.name
          adult_menu = True

    if kids_menu == True and adult_menu == True:
      return "{adult}\n{kids}".format(adult = formatting(name, items), kids = formatting("Kids", kids_items))
    elif adult_menu == True:
      return "{adult}".format(adult = formatting(name, items))
    else:
      return "CLOSED UNTIL 11:00 AM"


# ===== Business Class =====
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# ===== Menu Instances =====
brunch = Menu("Brunch",
{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11:00 am", "4:00 pm")
early_bird = Menu("Early Bird",
{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "4:00 pm", "6:00 pm")
dinner = Menu("Dinner",
{
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, "6:00 pm", "11:00 pm")
kids = Menu("Kids",
{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11:00 am", "9:00 pm")
arepas = Menu("Arepa",
{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10:00 am", "8:00 pm")     
            
# ===== Franchise Instances =====
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", arepas)
# ===== Business Instances =====
basta_fazoolin = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
take_a_arepa = Business("Take a' Arepa",arepas_place)

print(flagship_store.available_menus("12:00 pm"))
