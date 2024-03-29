import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #https://github.com/theskumar/python-dotenv#file-format#
from commands.dice import roll
from commands.randimage import randimage
from config import config
from command_prompt import command_prompt
from commands.callresponse import callresponse, addResponse, deleteResponse, editResponse
from commands.helpcommand import help

#i wonder if how you would have different versions of the bot for different servers would be having different initializations of the command prompt, and all it's objects.
#the token and shit is all just kinda the gateway to discord, the command_prompt() object is what is handling everything
#theres prob a better way to have the code that actually talks between discord and local computer.


#TODO determine how to save custom responses.
    #csv of command, response string.
    #load from that csv every time the bot executes
    #where to do this in the structure of things?
def main():
    #loading the .env
    load_dotenv() #loads the .env file (environment file)
    TOKEN = os.getenv('TOKEN') #gets the token from the environment file
    KEYWORD = os.getenv('KEYWORD') #sets the keyword for commands
    #config the .env on first load
    if TOKEN is None:
        config()


    #this is using the command pattern.
    cmnd = command_prompt(KEYWORD) #creates a command prompt

    #registering commands to the command prompt
    cmnd.add('roll', roll(''), 'where x is the number of dice, and n is the sides of the dice (1d6 for example)')
    cmnd.add('rollad', roll('ad'), 'roll with advantage')
    cmnd.add('rollda', roll('da'), 'roll with disadvantage')
    cmnd.add('woop', randimage(os.path.join("image_csvs", "woop_images.csv")), 'sends a random image of wooper') #the os.path.join() is necessary because linux uses / and windows uses \
    cmnd.add('miku', randimage(os.path.join("image_csvs", "miku_images.csv")), 'sends a random image of hatsune miku')
    cmnd.add('hello', callresponse('hello! :)'),'say hello to polonium!')
    cmnd.add('ar', addResponse(cmnd), 'add a custom response to the bot! format: ar <command> <response> where everything after the space is the response')
    cmnd.add('er', editResponse(cmnd), 'edit an already existing custom command! format: er <command> <new_response>')
    cmnd.add('dr', deleteResponse(cmnd), 'delete a custom response. format: dr <command>')
    cmnd.add('help', help(cmnd), 'prints a list of commands and their descriptions')
    cmnd.add('Custom Commands:',None,'')


    #establish connection to discord
    client = discord.Client()



    #async code that executes on a particular event
        #info about the async/await syntax: https://realpython.com/async-io-python/#

    @client.event
    async def on_ready(): #prints when the bot connects/reconnects to discord
        print('we have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        elif message.content.startswith(KEYWORD):
            messageInput = message.content.lstrip(KEYWORD) #strips the KEYWORD prefix from commands
            await message.channel.send(cmnd.find_and_execute(messageInput)) #finds and executes a command from the command prompt

    client.run(TOKEN)

if __name__  == "__main__":
    main()
#https://youtu.be/g_wlZ9IhbTs https://www.freecodecamp.org/news/if-name-main-python-example/ -- explanation of the def main if name main convention.
