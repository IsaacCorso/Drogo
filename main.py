# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

# imports
import replit
import os
import random
import discord
from discord.ext import commands
import time
from discord import app_commands
from discord.ext.commands.parameters import Author
import names
from monsters.monsters import Monster, monsters
from dndbeyond_websearch import Searcher
import requests
from bs4 import BeautifulSoup
from items.adventuregear import AdventureGear, adventuregear
from items.armor import Armor, armor
from items.weapons import Weapon, weapons
from character.races import Race, races
from character.classes import Class, classes
from replit import db
from easy_pil import Editor, load_image_async, Font
from discord import File
from selectmenubuttons.selectmenu import help 
# required discord stuff

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# defining prefix
p = 'a&'

# defining some stuff
def add_homebrew(homebrew_content):
  if "homebrew" in db.keys():
    homebrew = db['homebrew']
    homebrew.append(homebrew_content)
    db["homebrew"] = homebrew
  else:
    db['homebrew'] = [homebrew_content]
# category    
category_files = {
    'armor': 'categories/armor_homebrew.txt',
    'item': 'categories/item_homebrew.txt',
    'class': 'categories/class_homebrew.txt',
    'race': 'categories/race_homebrew.txt',
    'monster': 'categories/monster_homebrew.txt',
}
# console logging turning on


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Dungeons and Dragons'))
    print('We have logged in as {0.user}'.format(client))

# member join event
# @client.event
# async def on_member_join(member):

#   channel = member.guild.system_channel

#   background = Editor('cities-1.jpg')
#   profile_image = await load_image_async(str(member.avatar.url))

#   profile = Editor(profile_image).resize((150, 150)).circle_image()
#   poppins = Font.poppins(size=50, variant="bold")

#   poppins_small = Font.poppins(size=20, varian="light")

#   background.paste(profile, (325, 90))
#   background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)

#   background.text((400,260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
#   background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font="poppins_small", align="center")

#   file = File(fp=background.image_bytes, filename="cities-1.jpg")
#   await channel.send(f"Hello {member.mention}! Welcome to **{member.guild.name}**")
#   await channel.send(file=file)

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
    

      

#


# token



# Your bot token goes here
token = os.environ['token']
client.run(token)
