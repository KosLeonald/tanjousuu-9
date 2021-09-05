import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数２】\nあなたの心に強いストレスがかかっている様子が出ています。後でこんな風になったらよくないから、あれが心配だから、不安を消したいから・・・あらゆる不安や心配が心を占め、その予防のためにやるべき多くの事が身体を占め、あなたはもう一杯いっぱいですね。でも、不安や心配というのはそれがやって来てから対処をするので間に合います。先々の来るかどうか分からない事で悩むよりも、あなたの心の望むままに、「今」を生きてくださいね。"
option_2 = "【誕生数２】\nあなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」"
option_3 = "【誕生数２】\nあなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」"
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
