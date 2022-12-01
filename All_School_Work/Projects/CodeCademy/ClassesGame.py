#! Fighting Sandbox !#

class Player:
  def __init__(self, name, weapon, speed):
    self.name = name
    self.weapon = weapon
    self.speed = speed
    self.health = 100
    self.damage = 0
    if self.weapon == "Sword" or self.weapon == "sword":
      self.speed = self.speed + 2
      self.damage = 30
    if self.weapon == "Mace" or self.weapon == "mace":
      self.speed = self.speed - 4
      self.damage = 60
    if self.weapon != "Sword" and self.weapon != "sword" and self.weapon != "Mace" and self.weapon != "mace":
      self.speed = self.speed + 9
      self.damage = 5

  def __repr__(self):
    return f"\nYour name is {self.name}. You are equip with a {self.weapon} that deals {self.damage} damage and your speed it {self.speed}."

  def no_option(self):
    print(f"Thats not an option {self.name}. Try Again.")

  def attack(self):
    if boss.speed > player.speed:
      player.damage = player.damage - 5
      boss.health = boss.health - player.damage
      print(f"You Swing at the {boss.type} beast with your {player.weapon}. You deal {player.damage} damage because its faster than you. Enemy health is now {boss.health}.")

    elif boss.speed == player.speed:
      boss.health = boss.health - self.damage
      print(f"You Swing at the {boss.type} beast with your {player.weapon}. You deal {self.damage} damage. Enemy health is now {boss.health}.")

    else:
      self.damage = self.damage + 5
      boss.health = boss.health - self.damage
      print(f"You Swing at the {boss.type} beast with your {player.weapon}. You deal {self.damage} damage because your faster. Enemy health is now {boss.health}.")

  def heal(self):
    self.health = self.health + 20
    print(f"You heal yourself. health is now {self.health}")

  def dodge(self):
    print(f"You dodge")

class Boss:
  def __init__(self, type, speed, damage):
    self.type = type
    self.speed = speed
    self.damage = damage
    self.health = 100

  def __repr__(self):
    return f"Your enemy is a {self.type} type. Its speed is {self.speed} and its damage is {self.damage}."
  
  def boss_attack(self):
    if player.health <= 0:
      print("Your died.... Get better than return.")
      
    player.health = player.health - self.damage
    print(f"The enemy uses a {self.type} attack on you!, it deals {self.damage} damage!, Health is now {player.health}")


player_name = input("Welcome. Whats your name? ")
player_weapon = input("What Weapon would you like? Sword (DMG: 30 |SPD: +2) or a Mace (DMG: 60 |SPD: -4)? ")
player_speed = int(input("What is your speed (1-10)? "))

boss_type = input("\nWhat type of beast would you like to fight (Fire, Water, Wind)? ")
boss_damage = int(input("What is your desired enemy damage (1-100)? "))
boss_speed = int(input("What is your desired enemy speed (1-100)? "))

player = Player(player_name, player_weapon, player_speed)
boss = Boss(boss_type, boss_speed, boss_damage)

print(player)
print(boss)

def moves():
  choice = input('What your move (Attack, Heal or Dodge)? ')

  if choice == "Attack" or choice =="attack":
    player.attack()


  if choice == "Heal" or choice =="heal":
    player.heal()


  if choice == "Dodge" or choice =="Dodge":
    player.dodge()

  else:
    print(f"Thats not an option {player.name}. Try again")

moves()
boss.boss_attack()
moves()
boss.boss_attack()
moves()
boss.boss_attack()
moves()
boss.boss_attack()
moves()
boss.boss_attack()
moves()
boss.boss_attack()
moves()