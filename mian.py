import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数９】\nもしも今あなたが生き辛さや拘束感を感じて、息が詰まりそうな状態なら、それは自分で自分を縛っているからかも知れません。「９」のあなたは誠実で正直で、与えられたことは必ずやり遂げる意志の強さを持っています。けれどもあまりにも「こうあるべき」が強すぎてはいませんか？時には手抜きも息抜きも必要です。それは怠ける事ではなく、「建設的な柔軟さ」です。誰かの目や評価、ご機嫌など気にせず、あなたのやりやすい方法で生きてみてはいかがでしょうか♬"
option_2 = "【誕生数９】\nあなたは究極の選択を迫られている渦中でしょうか。右と左どちらを選ぶか。どちらを選んでも良い結果にはなりそうもない。でも選ばなければならない。にっちもさっちもいかない状況ですね💦でもよく目を凝らして見てみてください。あなたの前にある道は二つだけではありません。たくさんの道がさぁどうぞと拓けています。さぁしっかり選び自信をもって進んでくださいね。"
option_3 = "【誕生数９】\nあなたが近頃何にも楽しみを感じられず、自分の歓びから切り離されていることについて治療をしましょう。\nリラックスして、楽しんで、楽しい時が流れるままにしてください。人生は楽しむもので、我慢するものではありません。美味しい食べ物や良い音楽、親しい友人、楽しい娯楽などであなたの魂を歓ばせてあげてください。自分を甘やかしすぎるとか、心を奪われる事に躊躇しないで。\n\n「どれだけ、この歓びに抵抗できますか？」"
#option_4 = "確率分散 1"
#option_5 = "確率分散 2"
#option_6 = "確率分散 3"

def main():
    USER_ID = info['USER_ID']
    mylist = [ option_1,option_2,option_3]    
    messages1= TextSendMessage(random.choice(mylist))
    #messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")
    # today = datetime.datetime.fromtimestamp(time.time())
    #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages1)
     #   else :
    #line_bot_api.broadcast(messages2)  
    
if __name__ == "__main__" :
    main()
