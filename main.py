# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

# imports

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
        # Split the message content to get the roll description and additional value
        args = message.content.split()
        
        if len(args) < 2:
            await message.reply('Please specify the number of dice and sides (e.g., 2d12)')
            return

        roll_description = args[1]

        # Parse the roll description (e.g., "1d10")
        try:
            num_dice, sides = map(int, roll_description.split('d'))
        except ValueError:
            await message.reply('Invalid roll format. Please use XdY format (e.g., 2d10)')
            return

        if num_dice <= 0 or sides <= 0:
            await message.reply('Both the number of dice and sides must be greater than 0.')
            return

        # Check for advantage or disadvantage
        is_advantage = "adv" in args[2:]  # Check if "adv" is in the remaining arguments

        # Initialize variables
        rolls = []
        result = 0

        if is_advantage:
            # Advantage: Roll two dice and add the additional value to both
            for _ in range(2):
                roll = random.randint(1, sides)
                rolls.append(roll)
                result += roll
        else:
            # Normal roll: Roll a single die and add the additional value
            for _ in range(num_dice):
                roll = random.randint(1, sides)
                rolls.append(roll)
                result += roll

        # Check if there's an additional value (e.g., +3)
        additional_value = 0
        if len(args) > 2 and args[-1][0] == '+':
            try:
                additional_value = int(args[-1][1:])
                result += additional_value
            except ValueError:
                await message.reply('Invalid additional value. Please use +X format (e.g., +3)')

        await message.reply('Rolling the dice...')
        time.sleep(.7)
        await message.channel.send(f'<@{message.author.id}>, You rolled {num_dice}d{sides}{" with advantage" if is_advantage else ""}: Result: {result}, Rolls: {rolls}, Additional Value: {additional_value}')


# random names
    if message.content.startswith(f'{p}randomname'):
        args = message.content.split()
        
        # Check if the user specified a gender
        gender = None
        if len(args) > 1:
            gender_arg = args[1].lower()
            if gender_arg == 'male':
                gender = 'male'
            elif gender_arg == 'female':
                gender = 'female'

        # Check if the user specified 'full' for a full name
        full_name = False
        if len(args) > 2 and args[2].lower() == 'full':
            full_name = True

        # Generate a random name based on the specified gender and full name preference
        if full_name:
            generated_name = names.get_full_name(gender=gender)
        else:
            generated_name = names.get_first_name(gender=gender)
        
        # Determine the gender for the response message
        response_gender = "unspecified" if gender is None else gender
        response_name_type = "Full Name" if full_name else "First Name"
        await message.channel.send(f'Generated {response_gender.capitalize()} {response_name_type}: {generated_name}')
    if message.content.startswith(f'{p}rname'):
        args = message.content.split()
        
        # Check if the user specified a gender
        gender = None
        if len(args) > 1:
            gender_arg = args[1].lower()
            if gender_arg == 'male':
                gender = 'male'
            elif gender_arg == 'female':
                gender = 'female'

        # Check if the user specified 'full' for a full name
        full_name = False
        if len(args) > 2 and args[2].lower() == 'full':
            full_name = True

        # Generate a random name based on the specified gender and full name preference
        if full_name:
            generated_name = names.get_full_name(gender=gender)
        else:
            generated_name = names.get_first_name(gender=gender)
        
        # Determine the gender for the response message
        response_gender = "unspecified" if gender is None else gender
        response_name_type = "Full Name" if full_name else "First Name"
        await message.channel.send(f'Generated {response_gender.capitalize()} {response_name_type}: {generated_name}')

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


# add homebrew
    if message.content.startswith(f'{p}addhomebrew'):
      homebrew_content = message.content[len(f'{p}addhomebrew'):].strip()
      add_homebrew(homebrew_content)
      await message.reply(f'Embed Item Created, do `{p}listhomebrew`')
      return


    if message.content.startswith(f'{p}listhomebrew'):
      homebrew_content = []
      if "homebrew" in db.keys():
        homebrew_content = db["homebrew"]
      foo = ""
      for i in homebrew_content:
        foo += f'{i}, '
      await message.reply(foo)


    # if message.content.startswith(f'{p}homebrew'):
    #   homebrew_content = []
    #   if "homebrew" in db.keys():
    #     index = int(message.content.split(f'{p}homebrew',1)[1])
    #     homebrew_content = db["homebrew"]
    #   await message.reply(f'{homebrew_content(index)}')




  

# help command
    if message.content.startswith(f'{p}help'):
      embed = discord.Embed(
            title=f'Drogo Help Menu',
            description=f'`{p}roll` rolls a die or multiple dice \n`{p}randomname` generates a random name \n`{p}defeat` shows monster xp and image \n`{p}item` lookup any item in the players handbook \n`{p}race` shows any info on races \n`{p}class` shows any info on classes \n `{p}lookup` lookup anything from monsters, items, races, and classes',
            color=discord.Color.green(),
            timestamp=message.created_at,
          )
      await message.channel.send(embed=embed)
  
      
  

  
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
          await message.channel.send(f'Cannot find race: `{rest}`')
    

      

#


# token



# Your bot token goes here
token = os.environ['token']
client.run(token)
