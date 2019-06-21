#
# Simple Telegram Messenger
# @author: bartjan@pc-mania.nl
# Jun-21,2019
#
# https://github.com/barreljan/Telegram

import requests


class Messenger(object):
    def __init__(self, bot_id="", chat_id=""):
        if not bot_id:
            raise SystemExit('Missing `bot_id` during initiate')
        if not chat_id:
            raise SystemExit('Missing `chat_id` during initiate')
        self.api_bot_id = str(bot_id)
        self.api_chat_id = str(chat_id)
        self.api_endpoint = 'https://api.telegram.org/{}/sendMessage'.format(self.api_bot_id)

    def send(self, msg=""):
        if msg:
            _msg = str(msg)
        else:
            raise SystemExit('Message can not be empty')

        post_data = {'chat_id': self.api_chat_id,
                     'text': _msg}
        try:
            requests.post(url=self.api_endpoint, data=post_data)
        except:
            raise SystemExit('Something went wrong or can not connect to API...')

