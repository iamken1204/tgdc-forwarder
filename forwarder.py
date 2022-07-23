from telethon import TelegramClient, events
from telethon.tl.types import InputChannel
import discord
import asyncio
import os

message = None
image = None

TG_API_ID = os.environ['TG_API_ID']
TG_API_HASH = os.environ['TG_API_HASH']
DC_BOT_TOEKN = os.environ['DC_BOT_TOEKN']
DC_CHANNEL_ID = int(os.environ['DC_CHANNEL_ID'])
TG_CHANNEL_ID = int(os.environ['TG_CHANNEL_ID'])

"""
Telegram Client
"""
client = TelegramClient("forwardgram", TG_API_ID, TG_API_HASH)
client.start()

input_channels = []

# Find targeted chats
for d in client.iter_dialogs():
    if d.entity.id == TG_CHANNEL_ID:
        print("Input chat:", d.name, d.entity.id)
        input_channels.append(InputChannel(d.entity.id, d.entity.access_hash))
        break

print("Monitored chat IDs:")
for c in input_channels:
    print("\t", c.channel_id)

# Handle Telegram New Message Events


@client.on(events.NewMessage(chats=input_channels))
async def handler(event):

    if hasattr(event.media, 'photo'):
        await event.message.download_media(file='/app/img.jpg')
        print("handled tg photo")
        globals()['image'] = '/app/img.jpg'

    # If the message contains a URL, parse and send Message + URL
    try:
        parsed_response = (event.message.message + '\n' +
                           event.message.entities[0].url)
        parsed_response = ''.join(parsed_response)
    # Or we only send Message
    except:
        parsed_response = event.message.message

    print("handled tg message:", event.message.message)
    globals()['message'] = parsed_response


"""
Discord Client
"""
discord_client = discord.Client()


async def background_task():
    global message
    global image

    await discord_client.wait_until_ready()
    channel = discord_client.get_channel(DC_CHANNEL_ID)

    while True:
        if image:
            await channel.send(file=discord.File('/app/img.jpg'))
            image = None
        if message:
            await channel.send(message)
            message = None
        await asyncio.sleep(0.1)

discord_client.loop.create_task(background_task())


"""
Main process
"""
print("Listening now")
asyncio.run(discord_client.run(DC_BOT_TOEKN))
asyncio.run(client.run_until_disconnected())
