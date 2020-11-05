import const
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

bot = SimpleLongPollBot(tokens=const.token, group_id=const.id)

@bot.message_handler(bot.text_filter(("расписание", "Расписание")))
def echo(event: SimpleBotEvent) -> str:
    return "hello!"

bot.run_forever()