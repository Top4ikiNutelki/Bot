
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

vk = vk_api.VkApi(token="66a97041b8f14ec84cf994d197ef4cba186a7e3d3563b1e17251dd25433a5d98c653661e241a7bd787d39")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 192093581)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": event.object.text,
                                                "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                "random_id": 0})
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "пока":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": event.object.text,
                                                        "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "пока":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                        "random_id": 0})

