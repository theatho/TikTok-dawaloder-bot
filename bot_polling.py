## ها خير عاي شنو تدور ؟ 

import json
import requests
from requests import get,post
from system import Bot
from config import *

api = f"https://api.telegram.org/bot" + token_bot + "/"
update_id = 0

print("تم تشغيل البوت BY @SELVER7")
print("PRESS CTRL + C TO EXIT ")
while True:
	try:
		req = get(f"https://api.telegram.org/bot{token_bot}/getupdates",params={"offset":update_id}).json()
		if len(req['result']) == 0:
			continue
		try:
			update = req["result"][0]
#			for update in update:
			Bot(update)
			update_id = update['update_id'] + 1
			print("-"*40)
		except KeyError:
			continue
	except KeyboardInterrupt:
		exit()
	except requests.exceptions.ConnectionError:
		continue