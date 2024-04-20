import os
#from openai import OpenAI
from discord.ext import commands
import discord
import asyncio
from dotenv import load_dotenv
from pollqueue import Queue


def connect_to_discord():
    # This will function will the token for the bot so that we can give the bot other functions

    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.listen()
    async def on_message(message):
        if message.content == "!start" and message.author != bot.user:
            await message.channel.send("Okay, poll has started. You have 20 seconds to send an images using !poll \{image\}")

    @bot.command()
    async def start(ctx):  
        global poll_ongoing
        global poll_memes

        poll_ongoing = False    
        if not poll_ongoing:
            poll_ongoing = True
            poll_memes = Queue()
            await asyncio.sleep(20)
            await ctx.send("POLL DONE! Here are the images nerds:")
            if poll_memes:
                amount = 1
                while poll_memes.is_empty() == False:
                    msg = poll_memes.dequeue()
                    username = msg[0]
                    image = msg[1]
                    await ctx.send(f'[{amount}] by @{username}: ')
                    await ctx.send(image)
                    amount += 1
            else:
                await ctx.send("Bruh, no one even sent an image. Don't call me again losers.")
            poll_ongoing = False
        else:
            await ctx.send("Bro, a poll was already started....")

    @bot.command()
    async def poll(ctx, image):
        if poll_ongoing:
            poll_memes.enqueue((ctx.author.name, image))
        else:
            await ctx.send("Bruh, there isn't a poll active right now. Use !start to start one noob.")

            
        

    bot.run(discord_token)



def connect_to_dalle(token):
    if token is None:
        print("No token provided, exiting...")
        exit()  # Exit if no token is provided

    # Add the actual HTTP request code here
    pass
    # Using the CHATGPT OPEN AI API FOR CREATING IMAGES we will write this function using
    # HTTP post server/client requests

connect_to_discord()