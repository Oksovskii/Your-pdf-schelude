import const

from typing import Optional

from vkbottle import Keyboard, Text, GroupTypes, GroupEventType, VKAPIError
from vkbottle.bot import Bot, Message

bot = Bot(const.token)

KEYBOARD = Keyboard(one_time=True).add(Text("Расписание", {"cmd": "schelude"})).get_json()


@bot.on.message(text=["Расписание", "расписание", "Начать"])
@bot.on.message(payload={"cmd": "schelude"})
async def command_schelude(message: Message, item: Optional[str] = None):
    await message.answer(f"Расписание:", payload='rasp0001-1.jpg', keyboard=KEYBOARD)

bot.run_forever()