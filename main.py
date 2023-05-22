# pip install aiogram
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = 'YOUR TOKEN TELEGRAM'
openai.api_key = 'YOUR API TOKEN OPENAI'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    # settings
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.0,
        # max symbols
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])

# skip updates
executor.start_polling(dp, skip_updates=True)
