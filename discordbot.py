#discordbot.py MADE BY CeldServ(Daan)
import asyncio
import os
import discord
import time
import RPi.GPIO as GPIO
from discord import client
from discord.abc import _Undefined
from discord.ext import commands
from discord import Intents

intents = discord.Intents.default()
intents.members = True
currentStatus = 0

f = open("BotToken.key", "r")
token = f.readline()
f.close()

client = commands.Bot(command_prefix = "?" ,help_command=None, intents=intents)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(aliases=['Led'])
async def led(ctx):
    global currentStatus
    if currentStatus == 0:
        currentStatus = 1
        await ctx.send("Turned Led on!")
        GPIO.output(18, True)
    elif currentStatus == 1:
        currentStatus = 0
        await ctx.send("Turned Led off!")
        GPIO.output(18, False)

@client.command(aliases=['Blink'])
async def blink(ctx, arg):
    global currentStatus
    times = int(arg)
    if isinstance(times, int) and times < 11 :
        for x in range(times):
            await ctx.send("Blinking!")
            GPIO.output(18, True)
            print("On")
            time.sleep(0.5)
            GPIO.output(18, False)
            print("Off")
            time.sleep(0.5)
    else:
        await ctx.send("That is not a number, or the number is too big! Try again.")

client.run(token)

