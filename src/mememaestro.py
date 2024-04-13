import os
from openai import OpenAI
from discord.ext import commands


def connect_to_discord(token):
    # This will function will the token for the bot so that we can give the bot other functions
    pass


def connect_to_dalle(token):
    if token is None:
        print("No token provided, exiting...")
        exit()  # Exit if no token is provided

    # Add the actual HTTP request code here
    pass
    # Using the CHATGPT OPEN AI API FOR CREATING IMAGES we will write this function using
    # HTTP post server/client requests
