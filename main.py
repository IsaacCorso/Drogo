# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

# imports

import os
import random
import discord
from discord.ext import commands
import time
from discord import app_commands
import names
from monsters.monsters import Monster, monsters
# required discord stuff

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# defining prefix
p = 'a&'
# console logging turning on


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Dungeons and Dragons'))
    print('We have logged in as {0.user}'.format(client))

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
            await message.reply('Please specify the number of dice and sides (e.g., 2d10)')
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

#


# token



# Your bot token goes here
client.run('MTE1MDA0NjU5ODMyNDMxMDA5Ng.GdYkyH._-u4GoYt0JtfhMAPHu1vfIHoOIwcosONX6gfU4')
