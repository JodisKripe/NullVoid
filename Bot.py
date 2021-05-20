import os
from discord.ext import commands
from dotenv import load_dotenv
from datetime import date
import discord
import random


load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')
bot=commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if (guild.name==GUILD):
            break
    print("Data_env:")
    print(f'{bot.user} has connected to the following guild:\n{guild.name}\nid:{guild.id}')
    print("\nMembers:")
    for member in guild.members:
        print(member.name)
    #print(f'{client.user} has connected to Discord!')
    return
"""
@bot.event
async def on_message(message):
    if (message.author==bot.user):
        return
    if(message.content=="NullVoid"):
        response="Why so Serious? Have a toffee."
        await message.channel.send(response)
######################"""
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to the NullVoid.')
    return

@bot.command(name="NullVoid",help="Quotes Joker.")
async def quoteNullVoid(ctx):
    quotes=["Why So Serious?","Lets Not Blow this out of proportion"]
    response=quotes[random.randrange(0,len(quotes))]
    await ctx.send(response)

@bot.command(name="hi",help="Say hi to the Bot")
async def sayHi(ctx):
    await ctx.send("Hi")

@bot.command(name="intro",help="Bot Introduces Itself")
async def sayHi(ctx):
    await ctx.send("Hello. I am NullVoid.\nI perform elementary operations as of now but considering how smart my creators are, soon i will be able to do everything a bot possibly can.\n\nSee help to know what all i can do at the moment.")

@bot.command(name="date",help="Tells you the date")
async def tellDate(ctx):
    today = date.today()
    response="Today's Date is: " + str(today)
    await ctx.send(response)

@bot.command(name="dice",help="Roll a dice!")
async def Roll(ctx):
    response=random.randrange(1,7)
    await ctx.send(response)

@bot.command(name="create-channel",help="Creates channels")
@commands.has_role("Mod")
async def createChannel(ctx,channelName):
    guild=ctx.guild
    #print(channelName)
    existing_channel=discord.utils.get(guild.channels,name=channelName)
    #print(existing_channel)
    if not existing_channel:
        print(f'Creating a channel: {channelName}')
        await guild.create_text_channel(channelName)
        await ctx.send("Done!!")
    else:
        await ctx.send("Already exists :(")
"""
@bot.command(name="remove-channel",help="Remove a Channel")
@commands.has_role("Mod")
async def rmCh(ctx,channelName):
    existing_channel = discord.utils.get(ctx.guild.channels, name=channelName)
    if existing_channel:
        print(f'Removing channel: {channelName}')
        print(ctx.guild.channels)
        print(ctx.guild.get_channel(channelName))
        await ctx.guild.delete_channel(ctx.guild.get_channel(channelName))
        await ctx.send("Removed")
    else:
        await ctx.send("No such channel exists :(")
"""

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You dont have the permissions for this operation.")

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if(str(channel)=="general"):
            await channel.send(f"""Welcome to the end of the world, NullVoid {member.mention}""")

@bot.command(name="nuke",help="nukes the server")
@commands.has_role("Admin")
async def nuke(ctx, amount=10):
    if(amount<=500 and amount > 0):
        await ctx.message.channel.purge(limit=amount)
        await ctx.message.channel.send(f"Done! Attempted to delete {amount} messages!! B-)")
    else:
        await ctx.message.channel.send(f"Too Much for me :(")
bot.run(TOKEN)
