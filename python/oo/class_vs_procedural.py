heroName = 'Elsa'
heroHealth = 50
heroMagicPoints = 80
heroInventory = {'gold': 40, 'healing potion': 2, 'key': 1}
monsterName = 'Goblin'
monsterHealth = 20
monsterMagicPoints = 0
monsterInventory = {'gold': 12, 'dagger': 1}

print('The hero %s has %s health.' % (heroName, heroHealth))


class LivingThing():
    def __init__(self, name, health, magicPoints, inventory):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.inventory = inventory

# Create the LivingThing object for the hero.
hero = LivingThing('Elsa', 50, 80, {})
monsters = []
#monsters.append(LivingThing('Goblin', 20, 0, {'gold': 12, 'dagger': 1}))

#monsters.append(LivingThing('Dragon', 300, 200, {'gold': 890, 'magic amulet': 1}))
monsters = [LivingThing('Goblin', 20, 0, {'gold': 12, 'dagger': 1}), LivingThing('Dragon', 300, 200, {'gold': 890, 'magic amulet': 1})]

print('The hero %s has %s health.' % (hero.name, hero.health))
#print monsters
print('The monsters %s has %s health,' % (monsters.name))

