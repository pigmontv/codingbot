# 주석 쓰는법 # 또는 할 범위를 컨트롤 슬래시 
import discord 
import asyncio

client = discord.client()

token = "ODIyNzU3NDUzNzA2OTUyNzA0.YFW6lw.pzhNDodfA7C11zTkaL4LAV5vlpM"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('비쥬얼 스튜먹는중')
    await client.change_presence(status=discord.status.online, activity=game)

# @client.event
# async def on_message(message):
#     if message.content == "할말":
#         await message.channel.send("봇이 답할말")

client.run(token)