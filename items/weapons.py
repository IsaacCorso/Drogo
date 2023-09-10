class Weapon:
    def   __init__  (self, name, catagorie, cost, damage, weight, properties):
        self.name = name
        self.catagorie = catagorie
        self.cost = cost
        self.damage = damage
        self.weight = weight
        self.properties = properties


weapons = {
  
  'club': Weapon('Club', 'Simple Melee Weapon', '1 sp', '1d4 Bludgeoning', '2 lb.', 'Light'),
  'dagger': Weapon('Dagger', 'Simple Melee Weapon', '2 gp', '1d4 Piercing', '1 lb.', 'Finesse, Light, Thrown (range 20/60)'),
  'greatclub': Weapon('Greatclub', 'Simple Melee Weapon', '2 sp', '1d8 Bludgeoning', '10 lb.', 'Two-Handed'),
  'handaxe': Weapon('Handaxe', 'Simple Melee Weapon', '5 gp', '1d6 Slashing', '2 lb.', 'Light, Thrown (range 20/60)'),
  'javelin': Weapon('Javelin', 'Simple Melee Weapon', '5 sp', '1d6 Piercing', '2 lb.', 'Thrown (range 30/120)'),
  'light hammer': Weapon('Light Hammer', 'Simple Melee Weapon', '2 gp', '1d4 Bludgeoning', '2 lb.', 'Light, Thrown (range 20/60)'),
  'mace': Weapon('Mace', 'Simple Melee Weapon', '5 gp', '1d6 Bludgeoning', '4 lb.', '--'),
  'quarterstaff': Weapon('Quarterstaff', 'Simple Melee Weapon', '2 sp', '1d6 Bludgeoning', '4 lb.', 'Versatile (`&roll 1d8`)'),
  'sickle': Weapon('Sickle', 'Simple Melee Weapon', '1 gp', '1d4 Slashing', '2 lb.', 'Light'),
  'spear': Weapon('Spear', 'Simple Melee Weapon', '1 gp', '1d6 Piercing', '3 lb.', 'Thrown (range 20/60), Versatile (`&roll 1d8`)'),
  'light crossbow': Weapon('Light Crossbow', 'Simple Ranged Weapon', '25 gp', '1d8 Piercing', '5 lb.', 'Ammunition (range 80/320), Loading, Two-handed'),
  'dart': Weapon('Dart', 'Simple Ranged Weapon', '5 cp', '1d4 Piercing', '1/4 lb.', 'Finesse, Thrown (range 20/60)'),
  'shortbow': Weapon('Shortbow', 'Simple Ranged Weapon', '25 gp', '1d6 Piercing', '2 lb.', 'Ammunition (range 80/320), Two-handed'),
  'sling': Weapon('Sling', 'Simple Ranged Weapon', '1 sp', '1d4 Bludgeoning', '--', 'Ammunition (range 30/120)'),
  'battleaxe': Weapon('Battleaxe', 'Martial Melee Weapon', '10 gp', '1d8 Slashing', '4 lb.', 'Versatle (`&roll 1d10`)'),
  'flail': Weapon('Flail', 'Martial Melee Weapon', '10 gp', '1d8 Bludgeoning', '1/4 lb.', '--'),
  'glaive': Weapon('Glaive', 'Martial Melee Weapon', '20 gp', '1d10 Slashing', '6 lb.', 'Heavy, Reach, Two-handed'),
  'greataxe': Weapon('Greataxe', 'Martial Melee Weapon', '30 gp', '1d12 Slashing', '7 lb.', 'Heavy, Two-handed'),
  'greatsword': Weapon('Greatsword', 'Martial Melee Weapon', '50 gp', '2d6 Slashing', '6 lb.', 'Heavy, Two-handed'),
  'halberd': Weapon('Halberd', 'Martial Melee Weapon', '20 gp', '1d10 Slashing', '6 lb.', 'Heavy, Reach, Two-handed'),
  'lance': Weapon('Lance', 'Martial Melee Weapon', '10 gp', '1d12 Piercing', '4 lb.', 'Reach, Special'),
  'longsword': Weapon('Longsword', 'Martial Melee Weapon', '15 gp', '1d8 Slashing', '3 lb.', 'Versatle (`&roll 1d10`)'),
  'maul': Weapon('Maul', 'Martial Melee Weapon', '10 gp', '2d6 Slashing', '10 lb.', 'Heavy, Two-handed'),
  'morningstar': Weapon('Morningstar', 'Martial Melee Weapon', '15 gp', '1d8 Slashing', '4 lb.', '--'),
  'pike': Weapon('Pike', 'Martial Melee Weapon', '5 gp', '1d6 Piercing', '18 lb.', 'Heavy, Reach, Two-handed'),
  'rapier': Weapon('Rapier', 'Martial Melee Weapon', '25 gp', '1d8 Piercing', '4 lb.', 'Finesse'),
  'scimitar': Weapon('Scimitar', 'Martial Melee Weapon', '25 gp', '1d6 Slashing', '3 lb.', 'Finesse, Light'),
  'shortsword': Weapon('Shortsword', 'Martial Melee Weapon', '10 gp', '1d6 Piercing', '4 lb.', 'Finesse, Light'),
  'trident': Weapon('Trident', 'Martial Melee Weapon', '5 gp', '1d6 Piercing', '4 lb.', 'Thrown (Range 20/60), Versatile (`&roll 1d8`)'),
  'war pick': Weapon('War Pick', 'Martial Melee Weapon', '5 gp', '1d8 Piercing', '2 lb.', '--'),
  'warhammer': Weapon('Warhammer', 'Martial Melee Weapon', '5 gp', '1d8 Slashing', '2 lb.', 'Versatile (`&roll 1d10`)'),
  'whip': Weapon('Whip', 'Martial Melee Weapon', '2 gp', '1d4 Slashing', '3 lb.', 'Finesse, Reach'),
  'blowgun': Weapon('Blowgun', 'Martial Ranged Weapon', '10 gp', '1 Piercing', '1 lb.', 'Ammunition (Range 25/100), Loading'),
  'hand crossbow': Weapon('Hand Crossbow', 'Martial Ranged Weapon', '75 gp', '1d6 Piercing', '3 lb.', 'Ammunition (Range 30/120), Light, Loading'),
  'heavy crossbow': Weapon('Heavy Crossbow', 'Martial Ranged Weapon', '50 gp', '1d10 Piercing', '18 lb.', 'Ammunition (Range 100/400), Heavy, Loading, Two-handed'),
  'longbow': Weapon('Longbow', 'Martial Ranged Weapon', '50 gp', '1d8 Piercing', '18 lb.', 'Ammunition (Range 150/500), Heavy, Two-handed'),
  'net': Weapon('Net', 'Martial Ranged Weapon', '1 gp', '--', '3 lb.', 'Special, Thrown (Range 5/15)'),
                      
  
  
}