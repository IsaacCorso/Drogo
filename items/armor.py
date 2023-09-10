class Armor:
    def __init__(self, name, catagorie, cost, ac, strength, stealth, weight):
        self.name = name
        self.catagorie = catagorie
        self.cost = cost
        self.ac = ac
        self.strength = strength
        self.stealth = stealth
        self.weight = weight
        



armor = {
  'padded': Armor('Padded Armor', 'Light Armor', '5 gb', '11 + Dex Modifier', '--', 'Disadvantage', '8 lb.'),
  'leather': Armor('Leather Armor', 'Light Armor', '10 gb', '11 + Dex Modifier', '--', '--', '10 lb.'),
  'studded leather': Armor('Studded Leather Armor', 'Light Armor', '45 gb', '12 + Dex Modifier', '--', '--', '13 lb.'),
  'hide': Armor('Hide', 'Medium Armor', '10 gb', '12 + Dex Modifier (Max 2)', '--', '--', '12 lb.'),
  'chain shirt': Armor('Chain Shirt', 'Medium Armor', '50 gb', '13 + Dex Modifier (Max 2)', '--', '--', '20 lb.'),
  'scale_mail': Armor('Scale Mail Armor', 'Medium Armor', '50 gb', '14 + Dex Modifier (Max 2)', '--', 'Disadvantage', '45 lb.'),
  'breastplate': Armor('Breastplate Armor', 'Medium Armor', '400 gb', '14 + Dex Modifier (Max 2)', '--', '--', '20 lb.'),
  'half plate': Armor('Half Plate Armor', 'Medium Armor', '750 gb', '15 + Dex Modifier (Max 2)', '--', 'Disadvantage', '40 lb.'),
  'ring mail': Armor('Ring Mail Armor', 'Heavy Armor', '30 gb', '14', '--', 'Disadvantage', '40 lb.'),
  'chain mail': Armor('Chain Mail Armor', 'Heavy Armor', '75 gb', '16', '--', 'Disadvantage', '55 lb.'),
  'splint': Armor('Splint Armor', 'Heavy Armor', '200 gb', '17', '--', 'Disadvantage', '60 lb.'),
  'plate': Armor('Plate Armor', 'Heavy Armor', '1,500 gb', '18', '--', 'Disadvantage', '65 lb.'),
  'shield': Armor('Shield', 'Shield', '10 gb', '+2', '--', '--', '6 lb.')
  
  


  
}