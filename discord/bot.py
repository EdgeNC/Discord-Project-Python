import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hello_test = [
       'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Thanks For using my Bot, '
            'Welcome To My Discord Server'
        ),
    ]

    if message.content == 'doc':
        response = random.choice(hello_test)
        await message.channel.send(response)
    

client.run('')
