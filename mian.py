import json 
import random
#import time , datetime


from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    mylist = [
        
 "占い＆タイ式リラクゼーション グラターイ","占いをします"]
    messages1= TextSendMessage(random.choice(mylist))
    messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")

   # today = datetime.datetime.fromtimestamp(time.time())
   #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages)
     #   else :
    line_bot_api.broadcast(messages2)  

    
    
if __name__ == "__main__" :
    main()
