from unicodedata import name


sensors = {"living-Room":2, "Dining-Room":4, "Kitchen":6, "Basement":12, "Bedroom":1}
print(sensors)
living_Room = sensors["living-Room"]
print(f"The Living Room has {living_Room} sensors in it")
mr_sekol = {"name": "Mr. Sekol", "age":27, "kids":True}
print(mr_sekol)
print(mr_sekol["name"])

pasteries = {"Donuts":["Blueberry", "Cream Stick", "Boston Cream", "Glazed"], "cake":["Chocolate", "Vanilla", "Lemon", "Almond"], "cookies":["Chocolate Chip", "Oatmeal", "Lemon", "Peanut Butter"]}

print(pasteries)