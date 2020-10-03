# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')#sends ping

@client.command()
async def hotline(ctx):
    await ctx.send('Suicide Hotline: 800-273-8255')#suicide hotline

@client.command()
async def dating(ctx):
    await ctx.send('Dating Abuse and Domestic Violence Hotline:  866-331-9474')#dating abuse hotline

@client.command()
async def lgbtq(ctx):
    await ctx.send('The Trevor Project(LGBTQ Support Hotline):  866-488-7386')#LGBTQ Support

@client.command()
async def eating(ctx):
    await ctx.send('National Eating Disorder Association - Eating Disorder Hotline:  800-931-2237')#Eating Disorder

@client.command()
async def general(ctx):
    await ctx.send('General Crisis Hotline: text "SUPPORT" to 741-741 ')#General Crisis
    
@client.command()
async def mental(ctx):
    await ctx.send('National Alliance on Mental Illness - Mental Illness Hotline: 800-950-6264')#mental illness
     
@client.command()
async def sex(ctx):
    await ctx.send('Rape, Abuse and Incest National Network - Sexual Assault Hotline: 800-656-4673')#Sexual assault
 
@client.command(aliases=['veteran'])
async def vet(ctx):
    await ctx.send('Veterans Association - Veterans Crisis Hotline: 800-273-8255')#veteran crisis line
 
 @client.command(aliases=['abort'])
async def abortion(ctx):
    await ctx.send('National Domestic Violence Hotline - Abortion Hotline: 800-799-SAFE')#abortion hotline
 
 @client.command()
async def help(ctx):
    helptext = "```"
    for command in self.bot.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await ctx.send(helptext)#should return all commands

@client.command()
async def coronavirus():
    await ctx.send('Protect yourself from the virus! \
                    \n While 25 feet is recommended, be sure to try to stay at least \
                    6 feet from people you don\'t normally come in contact with! \
                    \n If you would like more information, feel free to call the CDC \
                    coronavirus hotline! : 1-800-CDC-INFO (1-800-232-4636)')

client.run(TOKEN)