import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import data
from datetime import datetime

# API-ключ созданный ранее
token = "66a97041b8f14ec84cf994d197ef4cba186a7e3d3563b1e17251dd25433a5d98c653661e241a7bd787d39"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
session_api = vk.get_api()
# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
while True:
    for event in longpoll.listen():

        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
            print(str(event.text))

