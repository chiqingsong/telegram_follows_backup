import json
from telethon import TelegramClient
import python_socks
import asyncio
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

api_id = ''  # Please replace with your API ID
api_hash = ''  # Please replace with your API Hash

async def main():
    client = TelegramClient(
        ''  # session name 
        ,api_id 
        ,api_hash
        #,proxy=(python_socks.ProxyType.SOCKS5, 'yourhost', yourportnumber) # If you need a proxy, fill in the host and port numbers.
    )

    async with client:
        await client.start()
        follows_backup = []

        async for dialog in client.iter_dialogs():
            if dialog.is_channel or dialog.is_group :
                entity = await client.get_entity(dialog.id)
                entity.access_hash = entity.access_hash if hasattr(entity, 'access_hash') else None
                entity.username = entity.username if hasattr(entity, 'username') else None

                item = {
                    "name": entity.title,
                    "id": entity.id,
                    "access_hash": entity.access_hash,
                    "type": "channel" if dialog.is_channel else "group",
                    "link": f"https://t.me/{entity.username}" if entity.username else "Private or no link"
                }
                follows_backup.append(item)
                print(item)
            
            if dialog.is_user :
                entity = await client.get_entity(dialog.id)
                bot =  entity.bot
                entity.access_hash = entity.access_hash if hasattr(entity, 'access_hash') else None
                entity.username = entity.username if hasattr(entity, 'username') else None
                item = {
                    "name": str(entity.first_name if entity.first_name is not None else "") + str(entity.last_name if entity.last_name is not None else ""),
                    "id": entity.id,
                    "access_hash": entity.access_hash,
                    "type": "User" if not bot else "bot",
                    "link": f"https://t.me/{entity.username}" if entity.username else f"The user phone number is:{entity.phone}"
                }
                follows_backup.append(item)
                print(item)
            
        with open('follows_backup.json', 'w',encoding='utf-8') as f:
            f.write(json.dumps(follows_backup, ensure_ascii=False, indent=2))

asyncio.run(main())