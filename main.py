from aiogram import Bot, Dispatcher, executor, types
from threading import Thread
import requests
import json
import asyncio

# ---config--- 
TOKEN = 'bot token'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# ---functions---
def get_info():
    url = "https://alerts.com.ua/api/states"
    headers = {"X-API-KEY": "your api key from alerts.com.ua"}
    response = requests.get(url, headers=headers)
    raw_json = response.json()
    return raw_json


# ---handlers---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello! I'm a bot that sends information about air alerts in the selected region. Write /help to learn more")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("commands: \n/alerts\n/ids\n/set_id\n/get_with_id")
    

@dp.message_handler(commands=['ids'])
async def send_ids(message: types.Message):
    json = get_info()
    parsed_json = json["states"]
    msg = ""
    for i in parsed_json:
        msg += i["name_en"] + " - " + str(i["id"]) + "\n"
    await message.reply(msg)


@dp.message_handler(commands=['alerts'])
async def send_alerts(message: types.Message):
    parsed_json = alerts_json["states"]
    msg = ""
    for i in parsed_json:
        msg += i["name_en"] + " - " + str(i["alert"]) + "\n"
    await message.reply(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)