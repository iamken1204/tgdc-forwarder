import asyncio
from telethon import TelegramClient, events
import discord
import os

TG_API_ID = os.environ['TG_API_ID']
TG_API_HASH = os.environ['TG_API_HASH']
DC_BOT_TOKEN = os.environ['DC_BOT_TOKEN']
DC_CHANNEL_ID = int(os.environ['DC_CHANNEL_ID'])
TG_CHANNEL_ID = int(os.environ['TG_CHANNEL_ID'])

client = TelegramClient("forwardgram", TG_API_ID, TG_API_HASH)
discord_client = discord.Client(intents=discord.Intents.all())
message_queue = asyncio.Queue()
discord_ready = asyncio.Event()

@client.on(events.NewMessage(chats=TG_CHANNEL_ID))
async def handler(event):
    if hasattr(event.media, 'photo'):
        await event.message.download_media(file='/app/img.jpg')
        await message_queue.put(('/app/img.jpg', 'image'))

    try:
        parsed_response = (event.message.message + '\n' +
                           event.message.entities[0].url)
    except:
        parsed_response = event.message.message

    print(f"Got message: {parsed_response}")
    await message_queue.put((parsed_response, 'text'))
    print("Message added to queue.")

async def background_task():
    await discord_ready.wait()
    channel = discord_client.get_channel(DC_CHANNEL_ID)
    print("Background task running...")

    while True:
        message, msg_type = await message_queue.get()
        if msg_type == 'text' and message == '':
            continue
        if message is None:
            continue
        print(f"Sending {msg_type}: {message}")
        if msg_type == 'image':
            await channel.send(file=discord.File(message))
        else:
            await channel.send(message)

@discord_client.event
async def on_ready():
    print("Discord client ready.")
    discord_ready.set()

async def main():
    await client.start()
    client_task = asyncio.create_task(client.run_until_disconnected())

    discord_client_task = asyncio.create_task(discord_client.start(DC_BOT_TOKEN))
    background_task_task = asyncio.create_task(background_task())

    await asyncio.gather(client_task, discord_client_task, background_task_task)

if __name__ == '__main__':
    asyncio.run(main())
