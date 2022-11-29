#!! Towe Defense !!#

import random
    
class Weapon:
  def __init__(self, name, ammo, damage):
    self.name = name
    self.ammo = ammo
    self.damage = damage

  def __repr__(self):
    print("You Choose the {name}. It has {ammo} rounds and causes {damage}".format(name = self.name))


  def reload(self):
    self.ammo == self.ammo + 1
    print("You Reloaded a bullet")

class Player:
  def __init__(self, name, weapon, shots_left):
    self.name = name
    self.weapon = weapon
    self.shots_left = shots_left

  def __repr__(self):
    return ""

  def fire(self):
    killed_enemies = random.radint(1, 250)
    self.ammo = self.ammo - 1
    print(f"Your Fired your weapon and killed {killed_enemies} enemies. Ammo is now {self.ammo}")

player_name = input("Hey! Whats your name soldier? ")
player_weapon = input("On your feet " + str(player_name) + "! Grab a weapon to defened the tower! Which one do you want? Rifle, Sniper or RPG? ")


if player_weapon != "Rifle" and player_weapon != "Sniper" and player_weapon != "RPG":
    player_weapon = input("Thats Not an option " + str(player_name) + "! Which one do you want? Rifle, Sniper or RPG? ")

elif player_weapon == "Rifle":
    Weapon("rifle", "60", "20")

elif player_weapon == "Sniper":
    Weapon("sniper", "15", "60")
    
    
elif player_weapon == "RPG":
    Weapon("rpg", "2", "2000")
    

player = Player(player_name, player_weapon, 0)

