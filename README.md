# Telegram to Discord Forwarder

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
