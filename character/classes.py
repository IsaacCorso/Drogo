class Class:
    def   __init__  (self, name, role, abilities, skills, hp, progression, subclasses, description):
        self.name = name
        self.role = role
        self.abilities = abilities
        self.skills = skills
        self.hp = hp
        self.progression = progression
        self.subclasses = subclasses
        self.description = description

    def __str__ (self):
        return f'**Name**: {self.name} \n**Role**: {self.role} \n**Abilities**: {self.abilities} \n**Skills**: {self.skills} \n**Hp**: {self.hp} \n**Progression**: {self.progression} \n**subclasses**: {self.subclasses} \n**Description**: {self.description}'

classes = {

  'barbarian': Class('Barbarian', 'Frontline Melee Combatant', 'Rage, Unarmored Defense, Reckless Attack, Danger Sense, Primal Path', 'Athletics, Intimidation', '1d12 hit points per level', 'Medium progression', 'Path of the Berserker, Path of the Totem Warrior, etc.', 'Barbarians are fierce warriors who channel their inner fury to become stronger in battle.'),
    'bard': Class('Bard', 'Support and Versatile Spellcaster', 'Bardic Inspiration, Spellcasting, Jack of All Trades', 'Choose any three skills', '1d8 hit points per level', 'Medium progression', 'College of Lore, College of Valor, etc.', 'Bards are charismatic performers and spellcasters who use their talents to inspire and manipulate others.'),
    'cleric': Class('Cleric', 'Divine Spellcaster and Healer', 'Divine Domain, Spellcasting, Channel Divinity', 'Religion, Medicine', '1d8 hit points per level', 'Medium progression', 'Life Domain, Light Domain, etc.', 'Clerics are devoted to a deity and serve as conduits of divine magic and healing.'),
    'druid': Class('Druid', 'Nature Spellcaster and Shapechanger', 'Wild Shape, Spellcasting, Druidic', 'Nature, Medicine', '1d8 hit points per level', 'Medium progression', 'Circle of the Land, Circle of the Moon, etc.', 'Druids are protectors of the natural world, harnessing the power of nature and transforming into animals.'),
    'fighter': Class('Fighter', 'Versatile Martial Warrior', 'Fighting Style, Second Wind, Action Surge', 'Choose any two skills', '1d10 hit points per level', 'Medium progression', 'Battle Master, Champion, etc.', 'Fighters are disciplined combatants skilled in various weapons and tactics.'),
    'monk': Class('Monk', 'Martial Artist and Unarmed Striker', 'Martial Arts, Ki, Unarmored Movement', 'Acrobatics, Stealth', '1d8 hit points per level', 'Medium progression', 'Way of the Open Hand, Way of the Shadow, etc.', 'Monks are masters of martial arts who harness inner energy to perform extraordinary feats and excel in unarmed combat.'),
    'paladin': Class('Paladin', 'Holy Warrior and Divine Spellcaster', 'Lay on Hands, Divine Smite, Divine Sense', 'Religion, Persuasion', '1d10 hit points per level', 'Medium progression', 'Oath of Devotion, Oath of Vengeance, etc.', 'Paladins are knights dedicated to upholding justice and righteousness, wielding divine powers in their quest.'),
    'ranger': Class('Ranger', 'Skilled Tracker and Nature Warrior', 'Favored Enemy, Natural Explorer, Primeval Awareness', 'Choose any three skills', '1d10 hit points per level', 'Medium progression', 'Hunter, Beast Master, etc.', 'Rangers are skilled outdoorsmen and hunters, with a strong connection to nature and the ability to track foes through any environment.'),
    'rogue': Class('Rogue', 'Stealthy and Cunning Adventurer', 'Sneak Attack, Cunning Action, Evasion', 'Choose any four skills', '1d8 hit points per level', 'Medium progression', 'Thief, Assassin, etc.', 'Rogues are masters of stealth and subterfuge, excelling in skills and precision attacks.'),
    'sorcerer': Class('Sorcerer', 'Innate Spellcaster and Magical Bloodline', 'Sorcerer Spellcasting, Sorcerous Origin, Font of Magic', 'Arcana, Persuasion', '1d6 hit points per level', 'Slow progression', 'Draconic Bloodline, Wild Magic, etc.', 'Sorcerers possess innate magical abilities, drawing power from their bloodlines or mysterious sources to cast spells.'),
    'warlock': Class('Warlock', 'Pact-bound Spellcaster and Eldritch Invoker', 'Eldritch Invocations, Pact Magic, Patron', 'Arcana, Deception', '1d8 hit points per level', 'Slow progression', 'The Fiend, The Great Old One, etc.', 'Warlocks form pacts with otherworldly entities to gain magical powers and dark secrets.'),
    'wizard': Class('Wizard', 'Scholarly Spellcaster and Arcane Researcher', 'Spellbook, Arcane Recovery, Ritual Casting', 'Arcana, History', '1d6 hit points per level', 'Slow progression', 'School of Evocation, School of Abjuration, etc.', 'Wizards are masters of arcane magic, specializing in spellcasting and the study of ancient knowledge and arcane spells.')
  
}