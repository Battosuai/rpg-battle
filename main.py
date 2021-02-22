from classes.game import Person, bcolors

magic = [
    {"name": "Fireball", "cost": 20, "damage": 35},
    {"name": "Solar Flare", "cost": 40, "damage": 50},
    {"name": "Hail Storm", "cost": 30, "damage": 40},
]

player = Person(100, 100, magic, 10, 15)
enemy = Person(100, 100, magic, 18, 6)

running = True

# print(player.genrateDamage())
# print(player.genrateDamage())
# print(player.genrateDamage())
# print(player.genrateDamage())

# print(player.generateSpellDamage(0))
# print(player.generateSpellDamage(1))
# print(player.generateSpellDamage(2))

print(bcolors.FAIL+bcolors.BOLD+"An Enemy Attacks!"+bcolors.ENDC)

while running:
    print("==================")
    player.chooseAction()
    choice = input("Choose action:")
    print("You choose", choice)
    index = int(choice) - 1

    if index == 0:
        dmg = player.genrateDamage()
        enemy.takeDamage(dmg)
        print("You attacked enemy for "+str(dmg) +
              " damage. Enemy got "+str(enemy.getHp())+" hp left")

        enemyChoice = 1

        enemyDmg = enemy.genrateDamage()
        player.takeDamage(enemyDmg)
        print("Enemy attacked you for "+str(enemyDmg) +
              " damage. You got "+str(player.getHp())+" hp left")

    # running = False
