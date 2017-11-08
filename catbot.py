import discord
import json,urllib
import urllib.request
import codecs
from urllib.request import urlopen

client = discord.Client()

def get_gif(message):
	req = urllib.request.urlopen("http://thecatapi.com/api/images/get?format=src&type=gif")
	finalurl = req.geturl()
	msg = finalurl.format(message)
	return msg
	
def get_cat(message):
	req = urllib.request.urlopen("http://thecatapi.com/api/images/get")
	finalurl = req.geturl()
	msg = finalurl.format(message)
	return msg

def get_fact():
	response = urlopen("https://catfact.ninja/fact").read().decode("utf8")
	j = json.loads(response)
	msg = j['fact']
	return msg
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return;	# no infinite loopies

	msg = ""
	command = message.content.lower()
	if command == '!catgif':
		msg = get_gif(message)
	elif command == '!cat':
		msg = get_cat(message)
	elif command == '!catfact':
		msg = get_fact()
	elif command == '!rules':
		msg = "http://lemons.party/i/rules.jpg"
	
	if(msg != ""):
		await client.send_message(message.channel, msg)
	
@client.event        
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

with open("settings.json") as data_file:
	data = json.load(data_file)

key = data["key"]
client.run(key)
