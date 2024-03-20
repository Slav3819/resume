import asyncio
from telethon import TelegramClient, events
import select_op


# Создаем клиента Telegram
api_id = 27706180 # Замените на свой API ID
api_hash = '8620397478d5ba319655e68caa7d3582' # Замените на свой API Hash
client = TelegramClient('my_session', api_id, api_hash)



# Устанавливаем параметры каналов
source_channel = 'https://t.me/+Lw8Prrady3k0YzEy' # Замените на имя источника
source_channel_two = '@Sperfektmoney' # Замените на второго имя источника
target_channel = '@slav_r' # Замените на имя целевого канала


# Обработчик события нового сообщения в источнике
@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    # Пересылаем сообщение в целевой канал
    await client.send_message(target_channel, event.message)
    print(event.message.message)

    # выполнение обработки сообщения
    select_op.ret_pp(event.message.message)

    # Ждем 1 секунд перед следующей пересылкой
    await asyncio.sleep(1)

# Обработчик события нового сообщения в источнике
@client.on(events.NewMessage(chats=source_channel_two))
async def handler_two(event):
    # Пересылаем сообщение в целевой канал
    await client.send_message(target_channel, event.message)
    print(event.message.message)

    #выполнение обработки сообщения
    select_op.ret_pp(event.message.message)

    #СООБЩЕНИЕ В КАНАЛ
    # await client.send_message(target_channel, select_op.ret_pp(event.message.message))

    # Ждем 1 секунд перед следующей пересылкой

    await asyncio.sleep(1)



# Запускаем клиента и ожидаем событий
with client:
    client.run_until_disconnected()




