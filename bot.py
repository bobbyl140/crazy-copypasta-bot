import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

crazyreply = "Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy."

@client.event
async def on_ready():
	print(f"{client.user} is ready and online!")

@client.event
async def on_message(message):
	if message.author.id != bot.application_id:
		if "crazy" in message.content.lower():
			await message.channel.send(crazyreply, reference=message)

client.run("TOKEN")