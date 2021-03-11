import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #this is a thing for the discord token. https://github.com/theskumar/python-dotenv#file-format#
from dice import dice_roll, xdn, dn
from randimage import randimage


#info about the async/await syntax:
    #https://realpython.com/async-io-python/#

load_dotenv() #loads all the files in from the .env file
TOKEN = os.getenv('DISCORD_TOKEN') #gets the token from the .env file

keyword = '.' #this is the keyword for commands

client = discord.Client()

woops = randimage('woop_images.csv')
mikus = randimage('miku_images.csv')

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #TODO is there a better way to handle keyword -> code then this structure? I need to check my 332S book

    #TODO implement .help
    #.help command -- COMING SOON -- returns a list of commands
    elif message.content.startswith(keyword + 'help'):
        diceInput = message.content.lstrip('.help ')
        await message.channel.send('coming soon')
   
    #.hello command -- returns "Hello!"
    elif message.content.startswith(keyword + 'hello'):
        await message.channel.send('hello! :)')

    #.rollad -- standard dice roller, with advantage
    elif message.content.startswith(keyword + 'rollad'):
        diceInput = message.content.lstrip('.rollad ')
        await message.channel.send(dice_roll(diceInput, 'ad'))

    #.rollda -- standard dice roller, with disadvantage
    elif message.content.startswith(keyword + 'rollda'):
        diceInput = message.content.lstrip('.rollda ')
        await message.channel.send(dice_roll(diceInput, 'da'))

    #.roll command -- standard dice roller
    elif message.content.startswith(keyword + 'roll'):
        diceInput = message.content.lstrip('.roll ')
        await message.channel.send(dice_roll(diceInput, ''))

    #.gme command -- returns a message about gamestop stock
    elif message.content.startswith(keyword + 'gme'):
        await(message.channel.send("\U0001F680 to the moon \U0001F680"))

    #.rblx command -- returns a message about roblox stock
    elif message.content.startswith(keyword + 'rblx'):
        await(message.channel.send("\U0001F680 stonks only go up \U0001F680"))

    #.miku command -- returns a link to the miku chug jug song
    elif message.content.startswith(keyword + 'miku'):
        await(message.channel.send(mikus.rand()))

    elif message.content.startswith(keyword + 'woop'):
        await(message.channel.send(woops.rand()))

client.run(TOKEN)