import discord
from bot_mantik import sifre_olusturucu

intents_discord = discord.Intents.default()
intents_discord.message_content = True


client = discord.Client(intents=intents_discord)

# @ başlarsa dekaratördür. dekartörler fonksiyonların çalışma işemini belirli olaylara göre değiştirir.
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!selam'):
        await message.channel.send('Merhaba Nasılsın?')
    elif message.content.startswith('!iyiyim'):
        await message.channel.send('İyi olduğuna sevindim!')
    elif message.content.startswith('!kötüyüm'):
        await message.channel.send('Senin için ne yapabilirim?')
    elif message.content.startswith('!şifre oluştur'):
        await message.channel.send(f'Senin için 10 Haneli Şifre Oluşturdum: {sifre_olusturucu(10)}')

client.run('')
