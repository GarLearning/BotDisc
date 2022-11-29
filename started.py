import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    """
    colocando bot online e retornando as seguintes mensagens:
    client.user.name: nome do bor
    client.user.id: nome do bot
    :return:
    """
    print("Bot Online")
    print(client.user.name)
    print(client.user.id)
    print("=" * 20)


#essa proxima função só é chamada quando digitase a chave no caso ?teste
@client.event
async def on_message(message):
    """
    1= bot retorna uma mensagen de textono mesmo canal escrito pelo usuario (?test)
    2= ao digitar o comando ?coin é conferido se o usuario, cargo, sala tem a permição requirida se sim e respondido
    com um jogo de cara ou coroa com emoji se n diz que n tem permição necessaria (?coin)
    :param message:
    :return:
    """
    if message.content.lower().startswith("?test"):
        await message.channel.send("hey, hey, heeeeyyyyy")

    if message.content.lower().startswith("?coin"):
        if message.author.id == 514210692635557890:
            choice = random.randint(1, 2)
            if choice == 1:
                await message.add_reaction("🙂")
            else:
                await message.add_reaction("👑")
        else:
            await message.channel.send("You don't have permission!")


client.run("NjM0NTgyNDUyODE1Mzk2ODgw.XccPkQ.5TT2J21h34bBb5_eI7uAbkiKrtA")