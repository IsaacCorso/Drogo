class Armor:
    def __init__(self, name, category, cost, ac, strength, stealth, weight):
        self.name = name
        self.category = category
        self.cost = cost
        self.ac = ac
        self.strength = strength
        self.stealth = stealth
        self.weight = weight

    def __str__ (self):
        return f'Name: {self.name}\nCategory: {self.category} \nCost: {self.cost} \nAc: {self.ac} \nStrength: {self.strength} \nStealth: {self.stealth} \nWeight: {self.weight}'
        



armor = {
  'padded armor': Armor('Padded Armor', 'Light Armor', '5 gb', '11 + Dex Modifier', '--', 'Disadvantage', '8 lb.'),
  'leather armor': Armor('Leather Armor', 'Light Armor', '10 gb', '11 + Dex Modifier', '--', '--', '10 lb.'),
  'studded leather armor': Armor('Studded Leather Armor', 'Light Armor', '45 gb', '12 + Dex Modifier', '--', '--', '13 lb.'),
  'hide': Armor('Hide', 'Medium Armor', '10 gb', '12 + Dex Modifier (Max 2)', '--', '--', '12 lb.'),
  'chain shirt': Armor('Chain Shirt', 'Medium Armor', '50 gb', '13 + Dex Modifier (Max 2)', '--', '--', '20 lb.'),
  'scale mail armor': Armor('Scale Mail Armor', 'Medium Armor', '50 gb', '14 + Dex Modifier (Max 2)', '--', 'Disadvantage', '45 lb.'),
  'breastplate': Armor('Breastplate Armor', 'Medium Armor', '400 gb', '14 + Dex Modifier (Max 2)', '--', '--', '20 lb.'),
  'half plate': Armor('Half Plate Armor', 'Medium Armor', '750 gb', '15 + Dex Modifier (Max 2)', '--', 'Disadvantage', '40 lb.'),
  'ring mail armor': Armor('Ring Mail Armor', 'Heavy Armor', '30 gb', '14', '--', 'Disadvantage', '40 lb.'),
  'chain mail armor': Armor('Chain Mail Armor', 'Heavy Armor', '75 gb', '16', '--', 'Disadvantage', '55 lb.'),
  'splint': Armor('Splint Armor', 'Heavy Armor', '200 gb', '17', '--', 'Disadvantage', '60 lb.'),
  'plate': Armor('Plate Armor', 'Heavy Armor', '1,500 gb', '18', '--', 'Disadvantage', '65 lb.'),
  'shield': Armor('Shield', 'Shield', '10 gb', '+2', '--', '--', '6 lb.')
  
  


  
}