# COMS W3132 Individual Project

## Author
Tobechi Onwuka
tio2003@barnard.edu,
Fahitza Quessa
fdq2000@barnard.edu



## Project Title
*Provide a short and descriptive title for your project.*

Name: Meme Maestro Bot

Discord Meme Bot that allows users within a discord server to start polls and send image prompts to generate meme images. 


## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or system.*

Example UI:

<img width="767" alt="Screenshot 2024-03-28 at 1 52 05 AM" src="https://github.com/coms-w3132/final-project-toonwuka04/assets/62598554/524d1dd7-aa5b-4822-96c4-03375a1ea59b">

Code Architecture:

<img width="765" alt="Screenshot 2024-03-28 at 1 52 10 AM" src="https://github.com/coms-w3132/final-project-toonwuka04/assets/62598554/fc8a891d-a641-4f51-b01b-18fe5085bba7">


## Additional Resources
*Include any additional resources, tutorials, or documentation that will be helpful for this project.*

→ [Discord Bot Documentation](https://discord.com/developers/docs/intro)
→ [Dalle API Documentation](https://openai.com/blog/dall-e-api-now-available-in-public-beta)


## Milestone 2 Goals
[Milestone2.pdf](https://github.com/coms-w3132/final-project-toonwuka04/files/14962603/Milestone2.pdf)

## Milestone 3 Demo:

<img width="582" alt="Screenshot 2024-04-27 at 1 08 00 AM" src="https://github.com/coms-w3132/final-project-toonwuka04/assets/62598554/cd665453-957b-43c2-9cf1-b574fabab5ee">

CONCLUSION:

HOW TO RUN MEMEMAESTRO IN DISCORD~
1. Join Messing Around With Memes Discord channel: https://discord.gg/78UR2aQc
2. Run MEMEMAESTRO.PY
	a. when running please make sure all libraries are properly installed, needed libraries include:
		- import os
		- from discord.ext import commands
		- import discord
		- import asyncio
		- from dotenv import load_dotenv
		- from pollqueue import Queue
		- import requests
   
  		 * Special instructions for PC users *
   * if you have a pc you must run this in the terminal: pip install python-dotenv
     to install from dotenv import load_dotenv *
     
4. Within the # bot-testing channel, type, !start, to start the program
5. To generate an image, type, !poll {insert_prompt}
6. Then wait for your image to load
7. Vote using reactions for your favorite images!

