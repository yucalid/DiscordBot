# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents = intents)

block_words = ["idiot", "ugly", "stupid"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg):
    if msg.author != client.user:
        for text in block_words:
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return

        print("Not Deleting...")


client.run('MTA3NDA1NTMwNTQ5Njg5MTQ4Mg.GHvXFV.eaORP8wBoqmuARRDoN8iyD3tkK0y2ED5TeeWwU')
