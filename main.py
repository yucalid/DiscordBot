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

    if message.content.startswith('hannah'):
        await message.channel.send('Hannah is cute!')

    elif message.content.startswith('bri'):
        await message.channel.send('bris1cal more like rizz1cal')

    elif len(message.content) > 1000:
        await message.channel.send('https://i.kym-cdn.com/photos/images/newsfeed/002/366/096/23e.png')

    elif message.content.startswith('mystic'):
        await message.channel.send('Why is mystic so horrible at Valorant?')

    elif message.content.startswith('ava'):
        await message.channel.send('Ava loves Sonali more than she loves Jonathan!')

    elif message.content.startswith('jay'):
        await message.channel.send('Jay really needs to loose some weight..')

    elif message.content.startswith('jon'):
        await message.channel.send('Jonathan is so massive that the military considers him a weapon.')

    elif message.content.startswith('kimber'):
        await message.channel.send('Everytime Kimberlina is in my eyesight, I drool uncontrollably.')

    elif message.content.startswith('alex'):
        await message.channel.send('Alex is such a cute little furry!')

    elif message.content.startswith('derek'):
        await message.channel.send('Derek is the WORST Valorant player of all time!')

    elif message.content.startswith('naito'):
        await message.channel.send('Naito is a human monkey.')

    elif message.content.startswith('star'):
        await message.channel.send('FATCOURS!')

    elif message.content.startswith('fps'):
        await message.channel.send('FPS guy is a literal idiot!')

    elif message.content.startswith('wezebi'):
        await message.channel.send('Wezebi is dumb.')

    elif message.content.startswith('zuig'):
        await message.channel.send('Zuig is literally fat.')

    elif message.content.startswith('sonali'):
        await message.channel.send('Sonali is our god, all hail Sonali.')

    elif message.content.startswith('caroline'):
        await message.channel.send('Caroline is adorable!')

    elif message.content.startswith('Positive message, please!'):
        await message.channel.send('Youre amazing!')

    elif message.content.startswith('avita'):
        await message.channel.send("HOTTIE AVITA")
   
client.run('MTA3NDA1NTMwNTQ5Njg5MTQ4Mg.GHvXFV.eaORP8wBoqmuARRDoN8iyD3tkK0y2ED5TeeWwU')
