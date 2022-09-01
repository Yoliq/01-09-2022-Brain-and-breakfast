# 01-09-2022-Brain-and-breakfast
Podklady pro Brain and breakfast 1. zari 2022

* Firstly bot has to be created in Telegram App, see https://www.youtube.com/watch?v=NwBWW8cNCP4 at 0:00-3:00 here API_KEY is obtained
* To send message using bot a receiver must start conversation with bot via Telegram App. Once conversation is started visit following website to retrieve chat_id: `https://api.telegram.org/bot<INSERT API KEY>/getUpdates`
    
* With API_KEY and conversation's chat_id Telegram_Bot instance is ready to be initialised and messages can be sent.

* More info: https://core.telegram.org/api
