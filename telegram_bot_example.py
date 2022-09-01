from telegram_bot import Telegram_Bot

'''
Example use case - setup Telgram_Bot instance and use it to send a message
'''

# SETUP BOT:
bot_api_key = 'insert API key here, str datatype'   # specify bot API key

bot_databazeChatID  =   {                           # chat ids for bot
                        '1st recipient name': 1111111111,
                        '2nd recipient name': 2222222222,
                        '3rd recipient name': 3333333333
                    }
bot = Telegram_Bot(bot_api_key, bot_databazeChatID)

# SEND MESSAGE USING BOT:
bot_mailbox = ['1st recipient name', '3rd recipient name'] # select recipients
message = 'sem napis zpravu co chces odeslat'   # define message
bot.sendMessage(bot_mailbox, message)


