import discord

TOKEN = 'WRITE TOKEN HERE'

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.content == 'Hello Bots!':
        await message.channel.send(f'Hello! Thank you call me!')


client.run(TOKEN)
