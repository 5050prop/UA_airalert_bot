from aiogram import Bot, Dispatcher, executor, types
import requests
import json
import asyncio

# ---config--- 
TOKEN = 'bot_token'
api_key = "api_key from alerts.com.ua"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# ---functions---
def get_info():
    url = "https://alerts.com.ua/api/states"
    headers = {"X-API-KEY": "{API_KEY}".format(API_KEY=api_key)}
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
    await message.reply("Vinnytsia oblast - 1\nVolyn oblast - 2\nDnipropetrovsk oblast - 3\nDonetsk oblast - 4\nZhytomyr oblast - 5\nZakarpattia oblast - 6\nZaporizhzhia oblast - 7\nIvano-Frankivsk oblast - 8\nKyiv oblast - 9\nKirovohrad oblast - 10\nLuhansk oblast - 11\nLviv oblast - 12\nMykolaiv oblast - 13\nOdesa oblast - 14\nPoltava oblast - 15\nRivne oblast - 16\nSumy oblast - 17\nTernopil oblast - 18\nKharkiv oblast - 19\nKherson oblast - 20\nKhmelnytskyi oblast - 21\nCherkasy oblast - 22\nChernivtsi oblast - 23\nChernihiv oblast - 24\nKyiv - 25")


@dp.message_handler(commands=['alerts'])
async def send_alerts(message: types.Message):
    json = get_info()
    parsed_json = json["states"]
    msg = ""
    for i in parsed_json:
        msg += str(i["name_en"]) + " - " + str(i["alert"]) + "\n"
    await message.reply(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)