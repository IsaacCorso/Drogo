class Race:
    def   __init__  (self, name, physicaltraits, abilityscorebonuses, lifespan, alignment, languages, subraces, specialabilities, description):
        self.name = name
        self.physicaltraits = physicaltraits
        self.abilityscorebonuses = abilityscorebonuses
        self.lifespan = lifespan
        self.alignment = alignment
        self.languages = languages
        self.subraces = subraces
        self.specialabilities = specialabilities
        self.description = description
      
    def __str__ (self):
        return f'**Name**: {self.name}\n**Physical Traits**: {self.physicaltraits} \n**Ability Score Bonuses**: {self.abilityscorebonuses} \n**Lifespan**: {self.lifespan} \n**Alignment**: {self.alignment} \n**Languages**: {self.languages} \n**Subraces**: {self.subraces} \n**Special Abilities**: {self.specialabilities} \n**Description**: {self.description}'

races = {
  'aarakocra': Race('Aarakocra', 'Bird-like humanoids with feathered wings and beaks.', '+2 Dexterity, +1 Wisdom', 'Around 30 years', 'Mostly neutral, tending towards good', 'Aarakocra, Auran', 'None', 'Flight (50 feet), Talon Attacks, Elemental Adept (Air)', 'Aarakocra are a race of bird-like humanoids who soar through the skies with their feathered wings. They are known for their keen eyesight and agility in the air, and they have a strong affinity for the elemental forces of air.'),
    'dragonborn': Race('Dragonborn', 'Physical traits for Dragonborn', '+2 Strength, +1 Charisma', 'Approximately 80 years', 'Varies', 'Languages spoken by Dragonborn', 'Subraces if applicable', 'Special abilities of Dragonborn', 'Description of the Dragonborn race'),
    'dwarf': Race('Dwarf', 'Physical traits for Dwarves', '+2 Constitution, +1 Wisdom', 'Over 300 years', 'Lawful good', 'Languages spoken by Dwarves', 'Hill Dwarf, Mountain Dwarf', 'Dwarven Resilience, Stonecunning, Dwarven Combat Training', 'Dwarves are a sturdy and resilient race known for their craftsmanship and underground cities.'),
    'elf': Race('Elf', 'Physical traits for Elves', '+2 Dexterity, +1 Intelligence', 'Around 750 years', 'Chaotic good', 'Languages spoken by Elves', 'High Elf, Wood Elf, Dark Elf (Drow)', 'Keen Senses, Fey Ancestry, Trance', 'Elves are an agile and graceful race with a deep connection to nature and magic.'),
    'genasi': Race('Genasi', 'Physical traits for Genasi', '+2 Constitution, +1 Intelligence', 'Varies', 'Varies', 'Languages spoken by Genasi', 'Air Genasi, Earth Genasi, Fire Genasi, Water Genasi', 'Elemental Resistance, Elemental Manifestation', 'Genasi are mortals with a touch of elemental power in their veins. They come in various elemental subtypes, each with unique abilities.'),
    'gnome': Race('Gnome', 'Physical traits for Gnomes', '+2 Intelligence, +1 Constitution', 'Around 350 years', 'Chaotic good', 'Languages spoken by Gnomes', 'Rock Gnome, Forest Gnome, Deep Gnome', 'Gnome Cunning, Artificer\'s Lore, Tinker', 'Gnomes are known for their curiosity, inventiveness, and love of tinkering. They often have a natural affinity for magic and a keen sense of humor.'),
    'goliath': Race('Goliath', 'Physical traits for Goliaths', '+2 Strength, +1 Constitution', 'Around 70 years', 'Mostly neutral', 'Languages spoken by Goliaths', 'None', 'Natural Athlete, Stone\'s Endurance, Powerful Build', 'Goliaths are massive and powerful humanoids known for their strength and endurance, often living in mountainous regions.'),
    'half-elf': Race('Half-Elf', 'Physical traits for Half-Elves', '+2 Charisma, +1 to two other ability scores of your choice', 'Around 180 years', 'Varies', 'Languages spoken by Half-Elves', 'None', 'Fey Ancestry, Skill Versatility', 'Half-Elves are a hybrid race with a mix of human and elf blood. They possess a blend of characteristics from both races.'),
    'half-orc': Race('Half-Orc', 'Physical traits for Half-Orcs', '+2 Strength, +1 Constitution', 'Around 75 years', 'Chaotic neutral', 'Languages spoken by Half-Orcs', 'None', 'Darkvision, Menacing, Relentless Endurance, Savage Attacks', 'Half-Orcs are a sturdy and resilient race known for their physical strength and determination.'),
    'halfling': Race('Halfling', 'Physical traits for Halflings', '+2 Dexterity, +1 Charisma', 'Around 150 years', 'Lawful good', 'Languages spoken by Halflings', 'Lightfoot Halfling, Stout Halfling', 'Lucky, Brave, Halfling Nimbleness', 'Halflings are small and nimble humanoids known for their luck and cheerful disposition.'),
    'human': Race('Human', 'Physical traits for Humans', '+1 to all ability scores', 'Around 70 years', 'Varies', 'Languages spoken by Humans', 'None', 'Versatile', 'Humans are adaptable and diverse, known for their versatility and ability to excel in various fields.'),
    'tiefling': Race('Tiefling', 'Physical traits for Tieflings', '+2 Charisma, +1 Intelligence', 'Around 80 years', 'Varies', 'Languages spoken by Tieflings', 'Variant Aasimar', 'Darkvision, Hellish Resistance, Infernal Legacy', 'Tieflings are descended from fiends, and they often bear a demonic appearance. They have a connection to the infernal plane and possess unique infernal abilities.'),
    'variant aasimar': Race('Variant Aasimar', 'Physical traits for Variant Aasimar', '+2 Charisma, +1 Wisdom', 'Around 100 years', 'Varies', 'Languages spoken by Variant Aasimar', 'None', 'Celestial Resistance, Celestial Legacy', 'Variant Aasimar are celestial beings with a radiant aura and celestial powers. They often have a strong connection to good-aligned deities and are guided by a sense of divine purpose.')
}
