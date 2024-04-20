import os
# from openai import OpenAI
from discord.ext import commands
import discord
import asyncio
from dotenv import load_dotenv
from pollqueue import Queue
import requests


def connect_to_dalle(token, prompt):
    if token is None:
        print("No token provided, exiting...")
        return  # Exit if no token is provided

    if not prompt:
        print("No prompt given by User...")
        return

    url = "https://api.openai.com/v1/images/generations"
    # Add the actual HTTP request code here
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    # Using the CHATGPT OPEN AI API FOR CREATING IMAGES we will write this function using
    # HTTP post server/client requests
    # boiler code from chat api
    data = {
        "model": "dall-e-2",  # specifying model in use
        "prompt": prompt,  # prompt we will get from user
        "n": 1,  # number of images to generate
        "size": "1024x1024"  # size allowed
    }
    response_req = requests.post(url, headers=headers, json=data)
    if response_req.status_code == 200:
        print("Image created")
        image_data = response_req.json()
        return image_data
    else:
        print(f"Image failed to generate: {response_req.status_code} {response_req.text}")
        return None


def connect_to_discord():
    # This will function will the token for the bot so that we can give the bot other functions

    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    api_token = os.getenv('FafaKey')

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)


    @bot.listen()
    async def on_message(message):
        if message.content == "!start" and message.author != bot.user:
            await message.channel.send(
                "Okay, poll has started. You have 20 seconds to send an image using !poll {image}")

    @bot.command()
    async def start(ctx):
        global poll_ongoing
        global poll_memes

        if not poll_ongoing:
            poll_ongoing = True
            poll_memes = Queue()
            await asyncio.sleep(20)

            if not poll_memes.is_empty():
                await ctx.send("POLL DONE! Here are the images nerds:")
                amount = 1
                while not poll_memes.is_empty():
                    username, image = poll_memes.dequeue()
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
        global poll_ongoing
        global poll_memes
        if poll_ongoing:
            poll_memes.enqueue((ctx.author.name, image))
        else:
            await ctx.send("Bruh, there isn't a poll active right now. Use !start to start one noob.")

    bot.run(discord_token)


connect_to_discord()
