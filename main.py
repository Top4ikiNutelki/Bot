from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from datetime import datetime
import time


def write_msg(peer_id, message):
    vk.method('messages.send', {'peer_id': peer_id, "random_id": 0, 'message': message})


token = "66a97041b8f14ec84cf994d197ef4cba186a7e3d3563b1e17251dd25433a5d98c653661e241a7bd787d39"
vk = vk_api.VkApi(token=token)
vk._auth_token()
vk_api = vk.get_api()
longpooll = VkBotLongPoll(vk, 192093581)

while True:
    for event in longpooll.listen():
        response = event.object.text.lower()
        if event.type == VkBotEventType.MESSAGE_NEW:
            if response == 'привет бот':
                write_msg(event.object.peer_id, "Привет =)")
            elif response == 'пока':
                write_msg(event.object.peer_id, "Пока")
            elif response == '!хелп' or response == '/help':
                write_msg(event.object.peer_id)




