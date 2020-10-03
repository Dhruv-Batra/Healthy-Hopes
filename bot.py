# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

class Warn{
    warned1Users = []
    warned2Users = []
    warned3Users = []
    bannedUsers = []

}

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.user.send('yo')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'kys' in message.content:
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kill urself' in message.content:
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kill yourself' in message.content:
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kms' in message.content:
        response = "Help is available, speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)

    if 'kill my self' in message.content:
        response = "Help is available, speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)

    if 'suicide' in message.content:
        response = "Help is available, Speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)

client.run(TOKEN)