#! Fighting Sandbox !#

class Chars:
  def __init__(self, name, weapon, speed, health = 100):
    self.name = name
    self.weapon = weapon
    self.speed = speed
    if weapon == "Sword" or weapon == "sword":
      self.weapondamage = 30
      self.speed = str(int(self.speed) + 2)
    if weapon == "Mace" or weapon == "mace":
      self.weapondamage = 50
      self.speed = str(int(self.speed) - 2)
    self.health = health
  
  def __repr__(self):
    return f"Your Name is {self.name}. You have a speed of {self.speed} and are equip with a {self.weapon}."

  def attack_boss(self):
    print(f"you swing your {self.weapon} at the beast!")

class Boss:
  def __init__(self, type, damage, speed):
    self.type = type
    self.damage = damage
    self.speed = speed
  
  def __repr__(self):
    return f"Your enemy is a {self.type} type. A beast with a speed of {self.speed} and causes {self.damage} damage per hit."

  def attack_player(self):
    print(f"The beast used a {self.type} attack!")


player1_name = input("Welcome to The Ring. Whats your name player? ")
player1_speed = int(input("On a scale of one to ten, how fast are you? "))
player1_damage= input("What weapon do you want? a Sword (dmg: 30 spd: +2) or a Mace (dmg: 50 spd: -2)? ")

player1 = Chars(player1_name, player1_damage, player1_speed)

boss_type = input("What enemy type would you like to fight (Fire, Wind or Water)? ")
boss_speed = int(input("On a scale of one to ten, how fast do you want it? "))
boss_damage= int(input("On a scale of one to ten, how strong do you want it? "))

boss = Boss(boss_type, boss_damage, boss_speed)

print(player1)
print(boss)

player1.attack_boss()
boss.attack_player()