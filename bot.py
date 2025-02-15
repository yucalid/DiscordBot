import discord

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)



client = commands.Bot(command_prefix='-', help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="I Am A Python Bot!"))
    print('I Have Awoken!')

@client.command(name='hi', aliases=['Hi'])
async def hi_cmd(ctx):
    await ctx.channel.send('hi bot user.')

@client.event
async def on_memeber_join(member):
    mbed = discord.Embed(
        colour = (discord.Colour.magenta()),
        tite = 'Welcome Message',
        description = f'Welcome {member.mention}, enjoy your stay!'
    )
    await member.send(embed=mbed)

token = 'MTA3NDA1NTMwNTQ5Njg5MTQ4Mg.GHvXFV.eaORP8wBoqmuARRDoN8iyD3tkK0y2ED5TeeWwU'

{
    client.run(token)
}