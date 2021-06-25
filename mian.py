import json 
import random
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    mylist = ["大吉","中吉","小吉","凶","大凶"]
    messages1= TextSendMessage(random.choice(mylist))
    messages= TextSendMessage(text="今日のあなたの運勢は" )
    messages2= TextSendMessage(text = "です。")
    line_bot_api.push_message(USER_ID,messages=messages + messages1 + messages2)
    line_bot_api.push_message(USER_ID,messages=messages1)
    line_bot_api.push_message(USER_ID,messages=messages2)
    
if __name__ == "__main__" :
    main()
