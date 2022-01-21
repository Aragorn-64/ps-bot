import discord
import os
import random
from replit import db
from collections import OrderedDict

client=discord.Client()

#defaults, incase users wish to reset
default_hello_inputs = ["%Hello", "%hello", "%Henlo", "%henlo"]
default_hello_outputs = ["Hello", "hello", "Henlo", "henlo", ]
default_smiles = [":grinning:", ":smiley:", ":slight_smile:", ":smile:", ":grin:"]

starter_hello_inputs = ["%hello", "%henlo"]
starter_hello_outputs = ["Hello", "hello", "Henlo", "henlo", ]
starter_smiles = [":grinning:", ":smiley:", ":slight_smile:", ":smile:", ":grin:"]

def update_db(key, value): #updating "key" db with "value"
  if key in db.keys():
    db1 = db[key]
    db1.append(value)
    db[key] = db1
  else:
    db[key] = [value]

#def delete_db(key, value):


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  in_options = starter_hello_inputs 
  if "hello in" in db.keys():
    in_options.extend(db["hello in"])
  
  #basic help guide
  if msg=="%help":
    await message.channel.send("""`ps-bot guide: \nGreet me ("%help inputs" to see the list of valid inputs) and I will reply ("-" to see a list of my replies)`""")

  if msg == "%help inputs":
    await message.channel.send("`ps-bot inputs:`")
    in_options = list(OrderedDict.fromkeys(in_options))
    await message.channel.send("`" + str(in_options) + "`")
    #i = 1
    #for x in in_options:
    #  await message.channel.send("`" + str(i) + ". " + x + ",`")
    #  i += 1
    await message.channel.send("`use - to add new inputs, and - to delete an input`")

  if msg.startswith("%new input"):
    new_input = msg.split("%new input ",1)[1]
    if new_input in db["hello in"]:
      await message.channel.send("Input is already recognized")
    else:  
      update_db("hello in",new_input)
      await message.channel.send(new_input + " added to list of valid inputs")

  if msg in in_options:
    #Replies to the %hello with Author username or nickname if set + a random smile:
    author_nick = str(message.author.nick)
    if author_nick == 'None':
      author = str(message.author)
      author = author.split('%')
      await message.channel.send( random.choice(starter_hello_outputs) + " " + author[0] + " " + random.choice(starter_smiles)) 
    else:
      await message.channel.send(random.choice(starter_hello_outputs) + " " + author_nick + " " + random.choice(starter_smiles))
    
client.run(os.environ['token'])

