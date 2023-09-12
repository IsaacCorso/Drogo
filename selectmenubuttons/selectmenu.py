import discord
class help(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a help Option", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Basic Commands",
                description="See a list of the Basic Commands"
            ),
            discord.SelectOption(
                label="Homebrew Content",
                description="See a list of Homebrew Content"
            ),
            discord.SelectOption(
                label="More Coming Soon",
                description="More Coming Soon"
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")