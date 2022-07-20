# Telegram to Discord Forwarder

## Prequisities

1. Apply Telegram app **api_id** & **api_hash**
   1. Create a new app at https://my.telegram.org/apps
   2. Record the **api_id** & **api_hash**
2. Apply Discord **bot token**
   1. Create a new application at [Discord Developer Portal](https://discord.com/developers/applications)
   2. Get in the bot just created
   3. Get in `Bot` at sidebar then click `Add bot`
   4. Get in `Reset Token`, record the token
   5. Get in `OAuth2` at sidebar, insert a valid URL into `Redirects`
   6. Get in `URL Generator` at sidebar, select `bot` & `Send Messages`, then scroll to the bottom of page
   7. Copy the generated URL and open it in another browser tab
   8. Follow the page's instructions to choose which channel you want the bot to join
3. Get Target Telegram **Chat ID** (**INPUT** target)
   1. Add this bot https://t.me/userinfobot in your Telegram
   2. **Forward** one of the target chat's message to @userinfobot
   3. Remove the **-100** from the start of Id and the rest is what you need
4. Get Target Discord **Chat ID** (**OUTPUT** target)
   1. Long press the target channel then click `Copy ID`

## How to Use

### Linux / Mac

```bash
docker run -it \
  -e TG_API_ID="your telegram api_id" \
  -e TG_API_HASH="your telegram api_hash" \
  -e DC_BOT_TOEKN="your discord bot token" \
  -e TG_CHANNEL_ID=1234567890 \
  -e DC_CHANNEL_ID=123456789012345678 \
  kettan/tgdc-forwarder

python3 forwarder.py
```

### Windows PowerShell

```powershell
docker run -it `
  -e TG_API_ID="your telegram api_id" `
  -e TG_API_HASH="your telegram api_hash" `
  -e DC_BOT_TOEKN="your discord bot token" `
  -e TG_CHANNEL_ID=1234567890 `
  -e DC_CHANNEL_ID=123456789012345678 `
  kettan/tgdc-forwarder

python3 forwarder.py
```

### Windows CMD

```
docker run -it ^
  -e TG_API_ID="your telegram api_id" ^
  -e TG_API_HASH="your telegram api_hash" ^
  -e DC_BOT_TOEKN="your discord bot token" ^
  -e TG_CHANNEL_ID=1234567890 ^
  -e DC_CHANNEL_ID=123456789012345678 ^
  kettan/tgdc-forwarder

python3 forwarder.py
```
