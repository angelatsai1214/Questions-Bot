import discord
import random
from questions import question_list
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$ask'):
    question = random.choice(question_list)
    await message.channel.send(question)

client.run(os.environ['TOKEN'])