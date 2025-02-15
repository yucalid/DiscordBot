# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    channel = await member.create_dm()
    await channel.send('Hi'+ member. name)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(len(message.content))
    if message.author == client.user:
        return

    if message.content.startswith('positive message please'):
        await message.channel.send('you are kind, you are smart, do not forget who you are.')

    if message.content.startswith('what do you think about me?'):
        await message.channel.send('I think you are a superstar!')

    if message.content.startswith(' im feeling sad today'):
        await message.channel.send('Should I direct you to a moderator! I hope everything is okay!')

    client.run('MTA3NDA1NTMwNTQ5Njg5MTQ4Mg.GHvXFV.eaORP8wBoqmuARRDoN8iyD3tkK0y2ED5TeeWwU')      