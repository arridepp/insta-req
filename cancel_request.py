from instagram_private_api import Client, ClientCompatPatch
import loginInfo
from random import randint
from time import sleep

api = Client(loginInfo.username, loginInfo.password)

open_file_txt = open("usersList.txt", "r").read().split("\n")

i = 0

for item in reversed(open_file_txt):
    if bool(item):
        user_info = api.username_info(item)
        uid = user_info['user']['pk']
        api.friendships_destroy(uid)
        i += 1
        randTime = randint(9, 22)
        setSleep = sleep(randTime)
        print("Follow request " + str(i) + " cancelled for: " + item +
              " | RANDOM TIME: " + str(randTime))
