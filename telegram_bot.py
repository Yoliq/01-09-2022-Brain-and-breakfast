class Telegram_Bot:
    '''
    Class used to control telegram bot using API interface
    First bot has to be created in Telegram App, see https://www.youtube.com/watch?v=NwBWW8cNCP4 at 0:00-3:00
        -   here API_KEY is obtained
    To send message using bot a receiver must start conversation with bot via Telegram App. Once conversation is started visit following website to retrieve chat_id:
        - https://api.telegram.org/bot<INSERT API KEY>/getUpdates
    
    With API_KEY and conversation's chat_id Telegram_Bot instance is ready to be initialised and messages can be sent.

    More info:
        - https://core.telegram.org/api
    '''
    
    def __init__(self, _api_key: str, contact_database: dict) -> None:
        self._api_key = _api_key
        self.contact_database = contact_database
        return None

    def addNewContacts(self, new_contacts: dict) -> None:
        self.contact_database.update(new_contacts)
        return None

    def deleteContacts(self, delete_contacts: tuple[str]) -> None:
        for contact in delete_contacts:
            self.contact_database.pop(contact)
        return None

    def _splitMessage(self, message: str) -> list[str]:
        '''Split long message into multiple smaller messages. This is because telegram has maximum message lenght.'''
        MAX_LEN = 4499
        split_message = []
        while True:
            if len(message) < MAX_LEN:
                split_message.append(message)
                break
            split_message.append(message[:MAX_LEN])
            message = message[MAX_LEN:]
        return split_message

    def _checkRecipient(self, recipient: str) -> None:
        if self.contact_database.get(recipient) == None:
            raise KeyError(f'Name {recipient} not defined in contact_database')
        return None

    def sendMessage(self, recipient_list: list, message: str) -> None:
        '''
        Sends message from message_list to each chat_id from recipients list
        '''
        import requests
        message_list = self._splitMessage(message)
        for recipient in recipient_list:
            self._checkRecipient(recipient)
            chat_id = self.contact_database[recipient]
            for message in message_list:
                url = f'https://api.telegram.org/bot{self._api_key}/sendMessage?chat_id={chat_id}&text={message}'
                requests.get(url)
        return None


