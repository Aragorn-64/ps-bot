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

def botout(text):
  #input a string and output in the format we use
  msgchan.send("`"+ text + "`")


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
  #Global varible for the message.channel
  global msgchan
  msgchan = message.channel 

  if message.author == client.user:
    return

  msg = message.content
  in_options = starter_hello_inputs 
  if "hello in" in db.keys():
    in_options.extend(db["hello in"])
  
  #maybe make an admin only %test command, that checks all commands and also cleans up after itself

  #basic help guide
  if msg=="%help":
    botout("""ps-bot guide: \nGreet me ("%help inputs" to see the list of valid inputs) and I will reply ("-" to see a list of my replies)""")

  if msg == "%help inputs":
    botout("Valid Inputs:")
    in_options = list(OrderedDict.fromkeys(in_options))
    #await msgchan.send("`"+ str(in_options) + "`")
    botout(str(in_options))
    botout("use %new input X to add new input X, and - to delete an input")

  if msg.startswith("%new input"):
    new_input = msg.split("%new input ",1)[1]
    if new_input in db["hello in"]:
      botout("Input is already recognized")
    else:  
      update_db("hello in",new_input)
      botout(new_input + " added to list of valid inputs")

  if msg in in_options:
    #Replies to the %hello with Author username or nickname if set + a random smile:
    author_nick = str(message.author.nick)
    if author_nick == 'None':
      author = str(message.author)
      author = author.split('%')
      botout( random.choice(starter_hello_outputs) + " " + author[0] + " " + random.choice(starter_smiles)) 
    else:
      botout(random.choice(starter_hello_outputs) + " " + author_nick + " " + random.choice(starter_smiles))
    
client.run(os.environ['token'])

