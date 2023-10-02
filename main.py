# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

# imports
import replit
import os
import re
import re
import random
import discord
from discord import Embed
from discord.ext import commands
import time
from discord import app_commands
from discord.ext.commands.parameters import Author
import names
from monsters.monsters import Monster, monsters
import requests
from bs4 import BeautifulSoup
from items.adventuregear import AdventureGear, adventuregear
from items.armor import Armor, armor
from items.weapons import Weapon, weapons
from character.races import Race, races
from character.classes import Class, classes
from easy_pil import Editor, load_image_async, Font
from discord import File
from selectmenubuttons.selectmenu import help
import json
from PIL import Image, ImageDraw, ImageFont
from bot_token import MY_TOKEN



user_campaigns = {}
campaigns = {}
used_campaign_names = {}
used_campaign_combinations = set()
used_passwords = set()
used_campaigns = set()
with open('campaigns.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 2:
            used_campaigns.add(parts[0])  # Assuming campaign name is the first element in each line
            used_passwords.add(parts[1])  # Assuming password is the second element in each line
# Initialize user_campaigns dictionary
user_campaigns = {}

# Read data from campaign_participation.txt and populate user_campaigns dictionary
with open('campaign_participation.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(' ')
        if len(data) >= 4:
            user_id, campaign_name, character_name, password = data[:4]
            user_campaigns[user_id] = campaign_name
            # You can optionally store character_name and password in your character_data dictionary for later use
        else:
            print(f"Invalid line in campaign_participation.txt: {line.strip()}. Skipping.")




# Read and process data from campaigns.txt file
# Read and process data from campaigns.txt file
# with open('campaigns.txt', 'r') as file:
#     for line in file:
#         parts = line.strip().split()
#         if len(parts) < 2:
#             print(f'Invalid line in campaigns.txt: {line.strip()}. Skipping.')
#             continue

#         name = parts[0]
#         password = parts[1]
#         creator_user_id = None
#         if len(parts) >= 3:
#             creator_user_id = parts[2]

#         # Process the data as needed, e.g., add it to the campaigns dictionary
#         campaigns[name] = {"password": password, "creator": creator_user_id}

from bot_token import MY_TOKEN


campaigns = {}
try:
    with open('campaigns.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            name, password = line.strip().split()
            campaigns[name] = password
except FileNotFoundError:
    campaigns = {}

def save_character_data():
    with open('character_data.json', 'w') as file:
        json.dump(character_data, file)

def load_character_data():
    try:
        with open('character_data.json', 'r') as file:
            bob = json.load(file)
            # print(bob)
            return bob
    except FileNotFoundError:
        print('not available')
        return {}

character_data = load_character_data()
# print('here i am')
# print(character_data)

# required discord stuff
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
# defining prefix
p = '&'

# # defining some stuff
   
category_files = {
    'armor': 'categories/armor_homebrew.txt',
    'item': 'categories/item_homebrew.txt',
    'class': 'categories/class_homebrew.txt',
    'race': 'categories/race_homebrew.txt',
    'monster': 'categories/monster_homebrew.txt',
}

# console logging turning on
# @tree.command(name="hello",
#               description="My first application Command",)
# async def command_hello(interaction):
#   await interaction.response.send_message("Hello Back!")
logo_file = discord.File("drogologo.png", filename="drogologo.png")

# invite command
@tree.command(name="invite",
              description="Invite Drogo to your Own Server"
             )
async def command_invite(interaction):
  embed = discord.Embed(
                title=f'Invite Drogo to your own Server',
                description='Invite Drogo to your own server with this link: [dsc.gg/drogo](https://dsc.gg/drogo)    \n \u200b \n Need help, Join the official Drogo help server at: [dsc.gg/drogoserver](https://dsc.gg/drogoserver)',
                color=discord.Color.orange(),
            )
  embed.set_footer(text= "Drogo - A Dungeons and Dragons discord bot", icon_url='attachment://drogologo.png')
  await interaction.response.send_message(file=logo_file, embed=embed)
  

@tree.command(name="roll",
              description="Roll command",)
async def command_roll(interaction, dice: str, advantage: bool=False,
                      additional_value: str="0"):
  """This command processes a roll.

    Parameters
    -----------
    dice: str
        The roll to execute
    advantage: bool
        True means this is an advantage roll
    additional_value: str
        +x or -x or 0 to add to the roll
  """

  roll_description = dice

  try:
    num_dice, sides = map(int, roll_description.split('d'))
  except ValueError:
    await interaction.response.send_message(
        'Invalid roll format. Please use XdY format (e.g., 2d10)')
    return

  if num_dice <= 0 or sides <= 0:
    await interaction.response.send_message(
        'Both the number of dice and sides must be greater than 0.')
    return

  is_advantage = advantage
  
  rolls = []
  result = 0

  if is_advantage:
    for _ in range(2):
      roll = random.randint(1, sides)
      rolls.append(roll)
    result = max(rolls)  # Take the higher of the two rolls
  else:
    for _ in range(num_dice):
      roll = random.randint(1, sides)
      rolls.append(roll)
      result += roll

  av = 0
  try:
    av = int(additional_value)
    if additional_value[0] == '-':
      result -= abs(av)  # Subtract the absolute value
    else:
      result += av
  except ValueError:
     await interaction.response.send_message(
         'Invalid additional value. Please use +X or -X format (e.g., +3 or -2)'
     )

  #await interaction.response.send_message('Rolling the dice...')
  #time.sleep(.7)
  await interaction.response.send_message(
      f'<@{interaction.user.id}>, You rolled {num_dice}d{sides}{" with advantage" if is_advantage else ""}: '
      f'Result: {result}, Rolls: {rolls}, Additional Value: {additional_value}'
      )



# @tree.command(name="randomname", description="Tells you a random name",guild=discord.Object(id=1147933019794046976))
# async def command_randomname(interaction, full_name: bool=False, gender: str=""):
#   """This command give you a random name.

#     Parameters
#     -----------
#     full_name: bool
#         Should i give you a full name
#     gender: str
#         What gender should the name be
#   """
#         # Check if the user specified 'full'
#         full_name = False
#         if len(args) > 1 and args[1].lower() == 'full':
#             full_name = True

#         # Check if the user specified a gender
#         gender = None
#         if len(args) > 2:
#             gender_arg = args[2].lower()
#             if gender_arg in ['male', 'm']:
#                 gender = 'male'
#             elif gender_arg in ['female', 'f']:
#                 gender = 'female'

#         # Check if a gender was specified for full names
#         if full_name and gender is None:
#             await message.channel.send('Please specify a gender for full names (e.g., male or female).')
#             return

#         # Generate a random name based on the specified gender
#         if full_name:
#             generated_name = names.get_full_name(gender=gender)
#             response_name_type = "Full Name"
#         else:
#             generated_name = names.get_first_name()
#             response_name_type = "First Name"

#         # Send the generated name along with the name type
#         await message.channel.send(f'Generated {response_name_type}: {generated_name}')



# @client.event
# async def on_member_join(member):
#     #pfp = member.user.avatar_url
#     embed = discord.Embed(
#       color = discord.Color.orange(),
#       title = f'Welcome {member.name}',
#       description = f'Hey {member.mention}\n \n**{member.guild.name}** Is Happy to Welcome you',
#     )
#     #embed.set_image(url=(pfp))

#     await client.get_channel(1147933020607762514).send(embed=embed)
    


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Dungeons and Dragons'))
    print('We have logged in as {0.user}'.format(client))
    await tree.sync()

    global character_data
    character_data = load_character_data()

# member join event
@client.event
async def on_member_join(member):

  channel = client.get_channel(1147933020607762514)

  background = Editor('cities-1.jpeg')
  profile_image = await load_image_async(str(member.avatar.url))

  profile = Editor(profile_image).resize((150, 150)).circle_image()
  poppins = Font.poppins(size=50, variant="bold")

  poppins_small = Font.poppins(size=20, variant="light")

  background.paste(profile, (325, 90))
  background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)

  background.text((400,260), f"{member.name}", color="white", font=poppins, align="center")
  background.text((400, 325), f"{member.name}#{member.discriminator}", color="black", font=poppins_small, align="center")

  file = File(fp=background.image_bytes, filename="cities-1.jpeg")
  await client.get_channel(1147933020607762514).send(f"Hello {member.mention}! Welcome to **{member.guild.name}**")
  await client.get_channel(1147933020607762514).send(file=file)

# commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #roll command
    if message.content.startswith(f'{p}roll'):
        args = message.content.split()

        if len(args) < 2:
            await message.reply('Please specify the number of dice and sides (e.g., 2d12)')
            return

        roll_description = args[1]

        try:
            num_dice, sides = map(int, roll_description.split('d'))
        except ValueError:
            await message.reply('Invalid roll format. Please use XdY format (e.g., 2d10)')
            return

        if num_dice <= 0 or sides <= 0:
            await message.reply('Both the number of dice and sides must be greater than 0.')
            return

        is_advantage = "adv" in args[2:]

        rolls = []
        result = 0

        if is_advantage:
            for _ in range(2):
                roll = random.randint(1, sides)
                rolls.append(roll)
            result = max(rolls)  # Take the higher of the two rolls
        else:
            for _ in range(num_dice):
                roll = random.randint(1, sides)
                rolls.append(roll)
                result += roll

        additional_value = 0
        if len(args) > 2 and (args[-1][0] == '+' or args[-1][0] == '-'):
            try:
                additional_value = int(args[-1])
                if args[-1][0] == '-':
                    result -= abs(additional_value)  # Subtract the absolute value
                else:
                    result += additional_value
            except ValueError:
                await message.reply('Invalid additional value. Please use +X or -X format (e.g., +3 or -2)')

        await message.reply('Rolling the dice...')
        time.sleep(.7)
        await message.channel.send(
            f'<@{message.author.id}>, You rolled {num_dice}d{sides}{" with advantage" if is_advantage else ""}: '
            f'Result: {result}, Rolls: {rolls}, Additional Value: {additional_value}')


# random names
    if message.content.startswith(f'{p}randomname') or message.content.startswith(f'{p}rname'):
        args = message.content.split()

        # Check if the user specified 'full'
        full_name = False
        if len(args) > 1 and args[1].lower() == 'full':
            full_name = True

        # Check if the user specified a gender
        gender = None
        if len(args) > 2:
            gender_arg = args[2].lower()
            if gender_arg in ['male', 'm']:
                gender = 'male'
            elif gender_arg in ['female', 'f']:
                gender = 'female'

        # Check if a gender was specified for full names
        if full_name and gender is None:
            await message.channel.send('Please specify a gender for full names (e.g., male or female).')
            return

        # Generate a random name based on the specified gender
        if full_name:
            generated_name = names.get_full_name(gender=gender)
            response_name_type = "Full Name"
        else:
            generated_name = names.get_first_name()
            response_name_type = "First Name"

        # Send the generated name along with the name type
        await message.channel.send(f'Generated {response_name_type}: {generated_name}')

# defeat command
    if message.content.startswith(f'{p}defeat'):
        rest = message.content[len(f'{p}defeat'):].strip().lower()
        if not rest:
            await message.channel.send(f"Please specify a monster's name after `{p}defeat`.")
            return
      
        monster = monsters.get(rest)

        if monster:
            embed = discord.Embed(
                title=f'You killed a(n) {monster.name}',
                description=f'You and your party gained {monster.xp} xp!',
                color=discord.Color.red(),
                timestamp=message.created_at,
            )
            embed.set_image(url=monster.image)
            await message.channel.send(embed=embed)

    # info command
    if message.content.startswith(f'{p}info'):
        rest = message.content[len(f'{p}info'):].strip().lower()
        if not rest:
            await message.reply(f'Please specify a monsters name after `{p}info`.')
            return

        monster = monsters.get(rest)

        if monster:
            embed = discord.Embed(
              title=f'Info for {monster.name}',
              description=f'{monster}',
              color=discord.Color.green(),
              timestamp=message.created_at,
              
              
            )
            embed.set_image(url=monster.image)
            await message.reply(embed=embed)

        if not monster:
            await message.reply(f'cannot find monster in `&info`, to see a list of monsters [go here](https://github.com/IsaacCorso/Drogo/blob/main/monsters/monsters.py)')


# monster image command
    if message.content.startswith(f'{p}mimage'):
        rest = message.content[len(f'{p}mimage'):].strip().lower()
        if not rest:
            await message.reply(f'Please specify a monsters name after `{p}mimage`.')
            return
          
        monster = monsters.get(rest)

        if monster:
            embed = discord.Embed(
              title=f'Image for `{monster.name}`:',
              color=discord.Color.orange()
            )
            embed.set_image(url=monster.image)
            await message.reply(embed=embed)
        if not monster:
            await message.reply(f'cannot find monster in `&mimage`, to see a list of monsters [go here](https://github.com/IsaacCorso/Drogo/blob/main/monsters/monsters.py)')

    
            
    # if message.content.startswith(f'{p}get_character_sheet'):
    #     # Extract the URL from the message
    #     try:
    #       url = message.content.split(' ')[1]
    #     except IndexError as e:
    #       await message.channel.send(f'Please include a url in `{p}get_character_sheet`')

    #     # Fetch the D&D Beyond character sheet
    #     character_sheet = fetch_character_sheet(url)

    #     if character_sheet:
    #         await message.channel.send(character_sheet)
    #     else:
    #         await message.channel.send("Unable to retrieve character sheet.")

    #     def fetch_character_sheet(url):
    #         try:
    #             # Fetch the HTML content of the D&D Beyond page
    #             response = requests.get(url)
    #             response.raise_for_status()

    #             # Parse the HTML with BeautifulSoup
    #             soup = BeautifulSoup(response.text, 'html.parser')

    #             # Extract character sheet information here
    #             # Example: character_name = soup.find('div', class_='character-name').text

    #             # Create a formatted character sheet string
    #             character_sheet = "Character Sheet Data Here"

    #             return character_sheet

    #         except Exception as e:
    #             print(f"Error fetching character sheet: {str(e)}")
    #             return None


  # item lookup command
    if message.content.startswith(f'{p}item'):
      rest = message.content[len(f'{p}item'):].strip().lower()
      if not rest:
          await message.channel.send(f"Please specify an item name after `{p}itemlookup`.")
          return

    # Check if the item exists in the adventure_gear dictionary
      item = adventuregear.get(rest)
      if not item:
        item = armor.get(rest)
      if not item:
        item = weapons.get(rest)
      if item:
            embed = discord.Embed(
                title=f'Info on {item.name}:',
                description=f'{item}',
                color=discord.Color.gold(),
                timestamp=message.created_at,
            )
            await message.channel.send(embed=embed)

      else:
          await message.channel.send(f'Cannot find item: `{rest}`')

# race lookup command
    if message.content.startswith(f'{p}race'):
      rest = message.content[len(f'{p}race'):].strip().lower()
      if not rest:
          await message.channel.send(f'Please specify a race name after `{p}race`.')
          return

      race = races.get(rest)


      if race:
          embed = discord.Embed(
            title=f'{race.name}',
            description=f'{race}',
            color=discord.Color.gold(),
            timestamp=message.created_at,
          )
          await message.channel.send(embed=embed)

      else:
          await message.channel.send(f'Cannot find race: `{rest}`')

# class lookup command
    if message.content.startswith(f'{p}class'):
      rest = message.content[len(f'{p}class'):].strip().lower()
      if not rest:
          await message.channel.send(f'Please specify a race name after `{p}class`.')
          return

      classs = classes.get(rest)


      if classs:
          embed = discord.Embed(
            title=f'{classs.name}',
            description=f'{classs}',
            color=discord.Color.gold(),
            timestamp=message.created_at,
          )
          await message.channel.send(embed=embed)

      else:
          await message.channel.send(f'Cannot find class: `{rest}`')

# ping command
    if message.content.startswith(f'{p}ping'):
        latency = round(client.latency * 1000) 
        await message.reply(f'Pong! Bot Latency: {latency}ms')


# random character stats command
    if message.content.startswith(f'{p}randstat') or message.content.startswith(f'{p}randstats') or message.content.startswith(f'{p}randomstats'):
        num_rolls = 6  # Number of times to roll the dice
        all_rolls = []  # Store all rolls

        for _ in range(num_rolls):
            # Roll 4 dice
            dice_rolls = [random.randint(1, 6) for _ in range(4)]

            # Sort the rolls in ascending order
            sorted_rolls = sorted(dice_rolls)

            # Remove the lowest roll
            lowest_roll = sorted_rolls[0]
            sorted_rolls.remove(lowest_roll)

            # Calculate the total
            total = sum(sorted_rolls)

            # Add the rolls to the list
            all_rolls.append({
                "rolls": dice_rolls,
                "total": total
            })

        # Calculate the total of all numbers excluding the lowest
        total_excluding_lowest = sum(roll["total"] for roll in all_rolls)

        # Create an embed for the results
        embed = discord.Embed(title="Random Stats Rolls", color=discord.Color.orange())

        for idx, roll_data in enumerate(all_rolls):
            rolls_formatted = [f"~~{roll}~~" if roll == min(roll_data["rolls"]) else str(roll) for roll in roll_data["rolls"]]
            rolls_message = ', '.join(rolls_formatted)
            response = f"Rolls {idx + 1}: {rolls_message} ({roll_data['total']})"

            embed.add_field(name=f"Stat {idx + 1}", value=response, inline=False)

        # Add the total excluding the lowest to the footer
        # embed = discord.Embed(title="Dice Rolls", color=discord.Color.orange())
        embed.set_footer(text=f"Total (excluding lowest): {total_excluding_lowest}")

        # Send the embed to the channel
        await message.reply(embed=embed)






  

# help command
    if message.content.startswith(f'{p}help'):
      embed = discord.Embed(
            title=f'Drogo Help Menu',
            description=f'`{p}roll` rolls a die or multiple dice \n`{p}randomname` generates a random name \n`{p}defeat` shows monster xp and image \n`{p}item` lookup any item in the players handbook \n`{p}race` shows any info on races \n`{p}class` shows any info on classes \n `{p}lookup` lookup anything from monsters, items, races, and classes',
            color=discord.Color.green(),
            timestamp=message.created_at,
          )
      await message.channel.send(embed=embed)
  
      



# add homebrew
    if message.content.startswith(f'{p}homebrewadd'):
        # Split the message into parts
        parts = message.content.split(None, 2)
        if len(parts) < 3:
            await message.channel.send(f"Invalid usage. Use `{p}homebrewadd [category] [content]`.")
            return

        _, category, homebrew_content = parts[:3]

        # Ensure the category is valid
        category = category.lower()
        if category not in category_files:
            await message.channel.send(f"Invalid category. Choose from: {', '.join(category_files.keys())}")
            return

        # Store the homebrew content in the respective file
        filename = category_files[category]
        with open(filename, "a") as file:
            file.write(homebrew_content + "\n")

        await message.channel.send(f"Homebrew {category} content added:\n{homebrew_content}")
# homebrew list
    elif message.content.startswith(f'{p}homebrewlist'):
        # Split the message into parts
        parts = message.content.split(None, 1)
        if len(parts) < 2:
            await message.channel.send(f"Invalid usage. Use `{p}homebrewlist [category]`.")
            return

        _, category = parts[:2]

        # Ensure the category is valid
        category = category.strip().lower()
        if category not in category_files:
            await message.channel.send(f"Invalid category. Choose from: {', '.join(category_files.keys())}")
            return

        # Retrieve the list of homebrew content from the respective file
        filename = category_files[category]
        homebrew_content = []
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                homebrew_content = file.readlines()

        if homebrew_content:
            # Send a list of all homebrew content in the specified category
            content_text = "".join(homebrew_content)
            await message.channel.send(f"Homebrew {category} content:\n{content_text}")
        else:
            await message.channel.send(f"No homebrew {category} content found.")
# homebrew search
    elif message.content.startswith(f'{p}homebrewsearch'):
        # Split the message into parts
        parts = message.content.split(None, 2)
        if len(parts) < 3:
            await message.channel.send(f"Invalid usage. Use `{p}homebrewsearch [category] [search term]`.")
            return

        _, category, search_term = parts[:3]

        # Ensure the category is valid
        category = category.strip().lower()
        if category not in category_files:
            await message.channel.send(f"Invalid category. Choose from: {', '.join(category_files.keys())}")
            return

        # Retrieve the list of homebrew content from the respective file
        filename = category_files[category]
        homebrew_content = []
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                homebrew_content = file.readlines()

        found_content = []
        for content in homebrew_content:
            if search_term.lower() in content.lower():
                found_content.append(content.strip())

        if found_content:
            # Send the list of found homebrew content in the specified category
            found_text = "\n".join(found_content)
            await message.channel.send(f"Found homebrew {category} content:\n{found_text}")
        else:
            await message.channel.send(f"No homebrew {category} content found matching: {search_term}")
  
  
# lookup command
    if message.content.startswith(f'{p}lookup'):
      rest = message.content[len(f'{p}lookup'):].strip().lower()
      if not rest:
        await message.channel.send(f'Please specify what you would like to lookup after `{p}lookup`')
        return

      lookup = monsters.get(rest)
      if not lookup:
        lookup = weapons.get(rest)
      if not lookup:
        lookup = armor.get(rest)
      if not lookup:
        lookup = adventuregear.get(rest)
      if not lookup:
        lookup = races.get(rest)
      if not lookup:
        lookup = classes.get(rest)

      if lookup:
          embed = discord.Embed(
            title=f'{lookup.name}',
            description=f'{lookup}',
            color=discord.Color.gold(),
            timestamp=message.created_at,
          )
          await message.channel.send(embed=embed)

      else:
          await message.channel.send(f'Cannot find: `{rest}`')
    

    official_races = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling"]
    official_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
     

#character creator command
    if message.content.startswith(f'{p}newcharacter'):
        command = message.content.split()
        if len(command) == 2:
            name = command[1]
            user_id = str(message.author.id)
            if user_id not in character_data:
                character_data[user_id] = []

            if any(char["name"].lower() == name.lower() for char in character_data[user_id]):
                await message.channel.send("You already have a character with that name.")
            else:
                character_data[user_id].append({
                    "name": name,
                    "race": "",
                    "class": "",
                    "items": [],
                    "spells": [],
                    "background": "",
                    "backstory": "",
                    "skills": {},
                    "armor_class": 0,
                    "max_health": 0,
                    "health": 0,
                    "speed": 0,
                    "initiative": 0,
                    "saving_throws": {},
                    "features_traits": "",
                    "proficiencies": [],
                    "languages": [],
                    "proficiency_bonus": 0,
                    "alignment": "",
                    "strength": "",
                    "strength_modifier": "",
                    "dexterity": "",
                    "dexterity_modifier": "",
                    "constitution": "",
                    "constitution_modifier": "",
                    "intelligence": "",
                    "intelligence_modifier": "",
                    "wisdom": "",
                    "wisdom_modifier": "",
                    "charisma": "",
                    "charisma_modifier": "",
                    "flaws": "",
                    "bonds": "",
                    "ideals": "",
                    "personality_traits": "",
                    "equipment": [],
                    "death_saves": {"successes": 0, "failures": 0},
                    "exp": 0,
                    "level": 1,
                    "treasure": "",
                    "allies_organizations": "",
                    "age": 0,
                    "height": "",
                    "weight": "",
                    "eyes": "",
                    "skin": "",
                    "hair": "",
                    "spellcasting_ability": "",
                    "spell_save_dc": 0,
                    "spell_attack_bonus": 0,
                    "homebrew": True
                })

                # After creating a character, save the character data
                save_character_data()
                await message.channel.send(f"Character `{name}` created.")
                await message.channel.send(f'Use `{p}editcharacter` to edit your character, and use `{p}characterinfo` to see character stats and info')

    if message.content.startswith(f'{p}editcharacter'):
        command = message.content.split()
        if len(command) == 1:
            await message.reply(f'Please include a name in `{p}editcharacter`')
        if len(command) == 2:
            await message.reply('Please specify a value, go to [Drogo Docs](https://drogo.gitbook.io/drogodocs/all-commands) to see a list of allowed values')
        if len(command) >= 4:
            name = command[1]
            thing = command[2].lower()  # Convert to lowercase for case-insensitive comparison
            value = ' '.join(command[3:])
            user_id = str(message.author.id)
            if user_id in character_data:
                for character in character_data[user_id]:
                    if character["name"].lower() == name.lower():
                        if thing == "race" and not character["homebrew"]:
                            await message.channel.send("Please enable homebrew to set a custom race.")
                            return
    
                        if thing in character:
                            character[thing] = value
                            # After editing the character, save the character data
                            save_character_data()
                            await message.channel.send(f"{thing.capitalize()} updated to {value}.")
                        else:
                            await message.reply(f'Cannot find `{thing}` in `{p}editcharacter`')
                        return
                await message.channel.send("Character not found.")
            else:
                await message.channel.send("You don't have any characters.")



  
    if message.content.startswith(f'{p}characterinfo'):
        command = message.content.split()
        if len(command) != 4 or not re.match(r'<@!?(\d+)>', command[2]):
            await message.channel.send(f"Please use the correct format: `{p}characterinfo <name> @user <category>`.")
            return
        name = command[1]
        player_ping = command[2]
        player_id_match = re.match(r'<@!?(\d+)>', player_ping)
        player = player_id_match.group(1)
        category = command[3]
    
        if player in character_data:
            for character in character_data[player]:
                if character["name"].lower() == name.lower():
                    embed = discord.Embed(title=f"Character Info for {name}", color=discord.Color.orange())
                    info_message = ""
                    if category.lower() == "all":
                        # Display all info
                        for key, value in character.items():
                            if key != "name":
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        info_message += f"{sub_key.capitalize()}: {sub_value}\n"
                                else:
                                    info_message += f"{key.capitalize()}: {value}\n"
                        # Split the info message into multiple embeds if it's too long
                        if len(info_message) > 2000:
                            chunks = [info_message[i:i + 2000] for i in range(0, len(info_message), 2000)]
                            for chunk in chunks:
                                embed.description = chunk
                                await message.channel.send(embed=embed)
                        else:
                            embed.description = info_message
                            await message.channel.send(embed=embed)
                        return
                    elif category.lower() == "stats":
                        # Display stats, hp, ac, exp, and stats
                        for key, value in character.items():
                            if key != "name" and key in ["hp", "ac", "exp", "stats"]:
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        info_message += f"{sub_key.capitalize()}: {sub_value}\n"
                                else:
                                    info_message += f"{key.capitalize()}: {value}\n"
                    elif category.lower() == "appearance":
                        # Display appearance, race, class, and background
                        for key, value in character.items():
                            if key != "name" and key in ["appearance", "race", "class", "background"]:
                                if isinstance(value, dict):
                                    for sub_key, sub_value in value.items():
                                        info_message += f"{sub_key.capitalize()}: {sub_value}\n"
                                else:
                                    info_message += f"{key.capitalize()}: {value}\n"
                    else:
                        await message.channel.send(f"Invalid category. Please use `{p}characterinfo <name> @user all`, `{p}characterinfo <name> @user stats`, or `{p}characterinfo <name> @user appearance`.")
                        return
                    # Display the info for the specified category
                    embed.description = info_message
                    await message.channel.send(embed=embed)
                    return
            await message.channel.send(f"Character '{name}' not found for the specified player.")
        else:
            await message.channel.send("Player not found or player has no characters.")
    

 # campaign commands
    if message.content.startswith(f'{p}campaign'):
        command = message.content.split(' ')
        if len(command) == 1:
            await message.channel.send('Please use a subcommand: create, join, or invite')
            return

        subcommand = command[1]

        if subcommand == 'create':
            if len(command) >= 4:
                name = command[2]
                password = command[3]
                creator_user_id = str(message.author.id)

                # Check if the user is already in a campaign
                if creator_user_id in user_campaigns:
                    await message.channel.send(f'You are already in a campaign: {user_campaigns[creator_user_id]}. You cannot create another campaign.')
                    return

                # Check if the campaign name and password are unique
                if name in used_campaigns and password in used_passwords:
                    await message.channel.send('A campaign with this name and password already exists. Please choose a different name and password.')
                    return

                # Rest of your code to create the campaign
                campaigns[name] = {"password": password, "creator": creator_user_id}
                with open('campaigns.txt', 'a') as file:
                    file.write(f'{name} {password} {creator_user_id}\n')

                # Add the used campaign name and password to the sets
                used_campaigns.add(name)
                used_passwords.add(password)
                print(f'Debug: Campaign name {name} and password {password} added to used sets.')

                # Associate the creator with the new campaign
                user_campaigns[creator_user_id] = name

                # Store participation information in campaign_participation.txt
                with open('campaign_participation.txt', 'a') as participation_file:
                    participation_file.write(f'{name} {creator_user_id}\n')

                await message.channel.send(f'Campaign "{name}" created with password "{password}". You have been automatically joined into this campaign.')
            else:
                await message.channel.send('Invalid command format. Please provide a name and a password for the campaign.')


        elif subcommand == 'join':
            if len(command) >= 5:
                character_name = command[2]
                campaign_name = command[3]
                password = command[4]
                user_id = str(message.author.id)

                # Check if the user is already in a campaign
                if user_id in user_campaigns:
                    await message.channel.send(f'You are already in a campaign: {user_campaigns[user_id]}. You cannot join another campaign.')
                    return

                # Check if the character exists and the campaign name and password are valid
                if character_name in character_data.get(user_id, []) and campaign_name in used_campaigns and password in used_passwords:
                    await message.channel.send('Invalid campaign name or password.')
                else:
                    # Add logic here for associating the character with the campaign
                    user_campaigns[user_id] = campaign_name
                    await message.channel.send(f'<@{user_id}> joined the Campaign "{campaign_name}" with the Character "{character_name}"!')

                    # Update campaign participation file with campaign, character, and password info
                    with open('campaign_participation.txt', 'a') as file:
                        file.write(f'{user_id} {campaign_name} {character_name} {password}\n')
                return

            await message.reply(f'Please use 3 arguments: `character_name`, `campaign_name`, `password`!')









        elif subcommand == 'leave':
            user_id = str(message.author.id)

            # Check if the user is in a campaign
            if user_id not in user_campaigns:
                await message.channel.send('You are not currently in any campaign.')
                return

            # Get the campaign the user is in and remove their association
            campaign_name = user_campaigns[user_id]
            del user_campaigns[user_id]

            # Update campaign participation file
            with open('campaign_participation.txt', 'w') as file:
                for user, campaign in user_campaigns.items():
                    file.write(f'{user} {campaign}\n')

            await message.channel.send(f'You have left the campaign "{campaign_name}".')



        elif subcommand == 'invite':
            if len(command) >= 3:
                person = command[2]
                person_formatted = ''.join(filter(str.isdigit, person))
                person_formatted = int(person_formatted)
                creator = message.author.mention
                await message.channel.send(f'{person_formatted}, {creator} has invited you to join a campaign!')
                await person_formatted.send("Hello, This is a Test Dm!")
              

        elif subcommand == 'delete':
            if len(command) >= 4:
                campaign_name = command[2]
                password = command[3]

                # Check if campaign exists and the provided password is correct
                if campaign_name in campaigns and campaigns[campaign_name] == password:
                    del campaigns[campaign_name]
                    with open('campaigns.txt', 'w') as file:
                        for name, pwd in campaigns.items():
                            file.write(f'{name} {pwd}\n')
                    await message.channel.send(f'Campaign "{campaign_name}" has been deleted.')
                else:
                    await message.channel.send('Invalid campaign name or password.')

        elif subcommand == 'info':
            user_id = str(message.author.id)

            # Check if the user is in a campaign
            if user_id not in user_campaigns:
                await message.channel.send('You are not currently in any campaign.')
                return

            # Get the user's current campaign and character name from the campaign_participation.txt file
            with open('campaign_participation.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(' ')
                    if len(data) >= 3 and data[0] == user_id:
                        campaign_name, character_name = data[1], data[2]
                        await message.reply(f'You are playing as `{character_name}` in the campaign `{campaign_name}`.')
                        return

            await message.channel.send('Unable to retrieve character information for the user.')


        








    # if message.content.startswith(f'{p}character_sheet'):
    #     name = message.content.split()[1]
    #     user_id = str(message.author.id)

    #     if user_id in character_data:
    #         for character in character_data[user_id]:
    #             if character["name"].lower() == name.lower():
    #                 sheet_width, sheet_height = 600, 800
    #                 sheet = Image.new('RGB', (sheet_width, sheet_height), 'white')
    #                 draw = ImageDraw.Draw(sheet)

    #                 font = ImageFont.truetype("arial.ttf", 24)

    #                 # Draw character information on the sheet
    #                 y_position = 50
    #                 for key, value in character.items():
    #                     if key != "name":
    #                         info_text = f"{key.capitalize()}: {value}"
    #                         draw.text((50, y_position), info_text, fill='black', font=font)
    #                         y_position += 50

    #                 sheet.save("character_sheet.png")

    #                 with open("character_sheet.png", "rb") as file:
    #                     character_sheet = discord.File(file)
    #                     await message.channel.send(file=character_sheet)
    #                 return
    #         await message.channel.send(f"Character '{name}' not found.")
    #     else:
    #         await message.channel.send("You don't have any characters.")




# token



# Your bot token goes here
client.run(MY_TOKEN)
