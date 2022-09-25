import discord


TOKEN = 'WRITE TOKEN HERE'


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.content == 'Hello Bots!':
        await message.channel.send(f'Hello! Thank you call me!')


client.run(TOKEN)
