#! Fighting Sandbox !#

class Player:
  def __init__(self, name, weapon, speed):
    self.name = name
    self.weapon = weapon
    self.speed = speed
    self.damage = 0
    if self.weapon == "Sword" or self.weapon == "sword":
      self.speed = self.speed + 2
      self.damage = 30
    if self.weapon == "Mace" or self.weapon == "mace":
      self.speed = self.speed - 4
      self.damage = 60
    else:
      self.speed = self.speed + 9
      self.damage = 5

  def __repr__(self):
    return f"Your name is {self.name}. You are equip with a {self.weapon} that deals {self.damage} damage and your speed it {self.speed}."

  def no_option(self):
    print(f"Thats not an option {self.name}. Try again. ")

  def attack_boss(self):
    print(f"You swing your {self.weapon} at the your enemy")

class Boss:
  def __init__(self, type, speed, damage):
    self.type = type
    self.speed = speed
    self.damage = damage

  def __repr__(self):
    return f"Your enemy is a {self.type} type. Its speed is {self.speed} and its damage is {self.damage}."


player_name = input("Welcome. Whats your name? ")
player_weapon = input("What Weapon would you like? Sword (DMG: 30, SPD: +2) or a Mace (DMG: 60 ,SPD: -4)? ")
player_speed = int(input("What is your speed (1-10)? "))

boss_type = input("What type of beast would you like to fight (Fire, Water, Wind)? ")
boss_damage = int(input("What is your desired enemy damage (1-10)? "))
boss_speed = int(input("What is your desired enemy speed (1-10)? "))

player = Player(player_name, player_weapon, player_speed)
boss = Boss(boss_type, boss_speed, boss_damage)

print(player)
print(boss)

choice = input('What your move (Attack, Heal or Dodge)')

while choice != "Attack" and choice != "attack" and choice != "Heal" and choice != "heal" and choice != "Dodge" and choice != "dodge":
  player.no_option()