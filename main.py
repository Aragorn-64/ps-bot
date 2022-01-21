import discord
import os
import random
from replit import db

client=discord.Client()

#defaults, incase users wish to reset
default_hello_inputs = ["Hello", "hello", "Henlo", "henlo"]
default_hello_outputs = ["Hello", "hello", "Henlo", "henlo", ]
default_smiles = [":grinning:", ":smiley:", ":slight_smile:", ":smile:", ":grin:"]

starter_hello_inputs = ["Hello", "hello", "Henlo", "henlo"]
starter_hello_outputs = ["Hello", "hello", "Henlo", "henlo", ]
starter_smiles = [":grinning:", ":smiley:", ":slight_smile:", ":smile:", ":grin:"]

def update_db(key, value):
  if key in db.keys():
    db1 = db[key]
    db1.append(value)
    db[key] = db1
  else:
    db[key] = [value]




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('#hello'):
    #Replies to the #hello with Author username or nickname if set + a random smile:
    author_nick = str(message.author.nick)
    if author_nick == 'None':
      author = str(message.author)
      author = author.split('#')
      await message.channel.send( random.choice(starter_hello_outputs) + " " + author[0] + " " + random.choice(starter_smiles))
      
    else:
      await message.channel.send(random.choice(starter_hello_outputs) + " " + author_nick + " " + random.choice(starter_smiles))
    
client.run(os.environ['token'])

