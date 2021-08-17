#from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('7GS55ur/ZBDmVoeJhDMupAphR9iHtvO9HiY4oidq9PH7HxxTzhzI9WQNYbaZPeMbEIwu82HhxPxm23oG7g56YBxSDKdVTeQKGjbVeCNTtZyQsDXegjd1N1o3Vq4jJ0hdEL2GO/TCPnPF4R+rNW4sTAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('37f4a61b28793e467570d6414dc83a96')

@app.route("/")
def test():
    return "OK"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

import re
import random

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if  event.message.text.isdecimal():
        result1 = re.sub(r"\D", "", event.message.text)

        #reply_message = "貴方の誕生月は「0」です。"
        result2 = sum(list(map(int,str(result1))))
        result3 = sum(list(map(int,str(result2))))
        result4 = sum(list(map(int,str(result3))))
        reply_message = f"貴方の誕生数は『{result4}』です"

    
    else:
        reply_message = f"貴方の文章内に文字が含まれています。"
    
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= reply_message))

    option_1 = ["これまでの人生の中で、あなたはいくつも姿を変えて今日まで来ました。何もかも人任せで自分というものがなかった時期があったかも知れませんし、ただ我武者羅に頑張ることだけにエネルギーを注いだ時期もあったかも知れません。紆余曲折を経て今、新たな平穏が訪れつつあるようです。あなたが直感で感じることと心で願う事が一致し、気後れしたり虚勢を張ったりする必要もなく、力を抜いてごく自然体でいられる、つまり本来のあなた自身に戻れる時のようです。","あなたは今、リーダーとしての役割を意識的に全面的に受け入れる時です。あなたの集中力、専心、安定感、鍛錬を通して、あなたは裏方から登場し、能力と知恵の両方で人々に認められるようになります。そして他の人は自然とあなたのカリスマ的波動に引き付けられあなたを信頼できると感じ、あなたの指導力に従うでしょう。あなたは自分の明るい光を世の中に放ち、あなたが他の人々を高みに導いていく際、その情熱や自信について語らなくてよいのです。\nただし自分に無理を課したり、燃え尽きてしまうことには注意してください。\n「自信を持ってリードしていきなさい」","あなたは今、リーダーとしての役割を意識的に全面的に受け入れる時です。あなたの集中力、専心、安定感、鍛錬を通して、あなたは裏方から登場し、能力と知恵の両方で人々に認められるようになります。そして他の人は自然とあなたのカリスマ的波動に引き付けられあなたを信頼できると感じ、あなたの指導力に従うでしょう。あなたは自分の明るい光を世の中に放ち、あなたが他の人々を高みに導いていく際、その情熱や自信について語らなくてよいのです。\nただし自分に無理を課したり、燃え尽きてしまうことには注意してください。\n「自信を持ってリードしていきなさい」"]
    option_2 = ["あなたの心に強いストレスがかかっている様子が出ています。後でこんな風になったらよくないから、あれが心配だから、不安を消したいから・・・あらゆる不安や心配が心を占め、その予防のためにやるべき多くの事が身体を占め、あなたはもう一杯いっぱいですね。でも、不安や心配というのはそれがやって来てから対処をするので間に合います。先々の来るかどうか分からない事で悩むよりも、あなたの心の望むままに、「今」を生きてくださいね。","あなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」","あなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」"]
    option_3 = ["これまであなたは難しい状況に屈することなく、あらゆる力を出して頑張ってきました。その成果が今にも現れようとしている時に、どうして自分を責めてしまっているのですか？自分の力不足や、他人への迷惑を思い、自己嫌悪に陥っているのでしょうか。そうであれば「３」の人らしい傾向ではありますが、誰もあなたに憤ってはいません。迷惑でもありません。さぁ頭を抱えて閉じた目を開けて、あなたがもたらした素晴らしい成果と称賛を受け取りましょう✨","あなたが人生に望む物は何でも作り出すことができますが、それはあなたが必要な仕事を自ら進んでしようとする時のみにできることです。そこには、近道も迂回路も無料のランチもないということです。\n成功するための唯一の道は、鍛錬し、やり続けるということです。あなたの目的を果たすために必要なことは何でも、自ら進んで行ってください。もし、自分がしなければならないことが何か分からない時は、それが何であるかを学びましょう。ハートと頭をオープンにして、あなたの基準を高く掲げてください。\n「いかなる分野においても、習熟するということは、あなた自身の中から最善だと思うものを求めることに他なりません」","あなたが人生に望む物は何でも作り出すことができますが、それはあなたが必要な仕事を自ら進んでしようとする時のみにできることです。そこには、近道も迂回路も無料のランチもないということです。\n成功するための唯一の道は、鍛錬し、やり続けるということです。あなたの目的を果たすために必要なことは何でも、自ら進んで行ってください。もし、自分がしなければならないことが何か分からない時は、それが何であるかを学びましょう。ハートと頭をオープンにして、あなたの基準を高く掲げてください。\n「いかなる分野においても、習熟するということは、あなた自身の中から最善だと思うものを求めることに他なりません」"]
    option_4 = ["あなたの心の声に耳を傾けてください。誰かの迷惑や噂や評価、顔色などを全く気にしなくてよい状況ならあなたはどんな答えを出すか、その声を聴いてみてください。本当はきっとあなたには分かっているのではないでしょうか。自分が何をしたいか、どう動きたいか。もしもそれが実行出来ていないとしたら、周りの環境のせいではなく、あなた自身への信頼不足なだけでしょう。今は、自分の心の声に素直になること、自分を信じてそれに飛び込んで行くことです。","今この時期は、緊急性があるという想像に基づいて行動を取るときではありません。感情があなたと共に流れ出るのを止めてください。あなたの理性の力をしっかりと持ち、目の前のドラマやこの瞬間の激しさから遠ざかりたいという気持ちを信頼しましょう。あなたのハイヤー・セルフが、あなたを正しい結論へ誘導してくれるのに任せましょう。\nその結論を心に抱いて眠りにつき、さらには、その結論を心に抱いて三夜眠り、ハイヤー・セルフのメッセージを心に留めましょう。\n「今は、ハイヤー・セルフにそれを任せてください」\n（ハイヤー・セルフとは、あなたの中に在る本当のあなた、なにが真実かを知っているあなたのことです）","今この時期は、緊急性があるという想像に基づいて行動を取るときではありません。感情があなたと共に流れ出るのを止めてください。あなたの理性の力をしっかりと持ち、目の前のドラマやこの瞬間の激しさから遠ざかりたいという気持ちを信頼しましょう。あなたのハイヤー・セルフが、あなたを正しい結論へ誘導してくれるのに任せましょう。\nその結論を心に抱いて眠りにつき、さらには、その結論を心に抱いて三夜眠り、ハイヤー・セルフのメッセージを心に留めましょう。\n「今は、ハイヤー・セルフにそれを任せてください」\n（ハイヤー・セルフとは、あなたの中に在る本当のあなた、なにが真実かを知っているあなたのことです）"]
    option_5 = ["あなたを優雅さと気楽さが満たそうとしています。あなたは自分の目的と繋がり、あなたが鍛錬を積んで注力してきたことが実を結びます。単なる幸運を超えたかたちで。\n自分の瞬間的な衝動を信頼し、躊躇することなくそれに乗って行動しましょう。あなたの最大の課題は、この楽しく自然で健康的な自尊心をしっかりと保ち、他人に横槍をいれさせないことです。\nあなたの夢、あなたのスピリット、あなた自身を信じましょう。\n「優雅に歩きなさい。万事上手くいきます」","今週は、あなたの情熱を注げることに対して行動することがカギとなるようです。その情熱は今はもう手放してしまっていること、あるいはその胸の内に抑え込んでいる事かも知れません。今もホットな状態で維持しているものの可能性もあります。あなたのエネルギーの中心にあって、マグマのように熱くうごめいているその情熱を今週は思い切り出していきましょう。迷いを捨ててワクワクする時です。情熱と共に光をまとって突き進みましょう。","あなたを優雅さと気楽さが満たそうとしています。あなたは自分の目的と繋がり、あなたが鍛錬を積んで注力してきたことが実を結びます。単なる幸運を超えたかたちで。\n自分の瞬間的な衝動を信頼し、躊躇することなくそれに乗って行動しましょう。あなたの最大の課題は、この楽しく自然で健康的な自尊心をしっかりと保ち、他人に横槍をいれさせないことです。\nあなたの夢、あなたのスピリット、あなた自身を信じましょう。\n「優雅に歩きなさい。万事上手くいきます」"]
    option_6 = ["痛みと苦しみに耐えていた時期が過ぎて、あなたの前に新たな展開、展望が広がってきました。これまで辛かった分を上回るほど、あなたは新たな展開に大きく期待が出来ますし、現在のところに留まらず、どこへでも飛んで行ける自由さも手に入れました。閉ざされ引き止められていた自分の根から起き上がり、これからはあまり深刻にならずに、もっともっと人生を楽しむ方向に舵を切りましょう。明るいきらめきの世界が広がっていることを信じてください。","あなたは、偉大な発展と祝福の時期に入りました。あなたは、豊穣、祝福、歓待の季節にいざなわれています。今こそ、人生があなたにその実りで報いる時期なのです。あなたは婚約したり、結婚したり、昇格したり、何かを獲得したり、あるいは長く待たれたラッキーな休暇を得るかも知れません。\nあなたが何を望もうとも、確実にそれが来ているので準備をしましょう。人生の潮の流れがあなたの方へ向いてきており、それはあなたがしっかりと努力をしてきたことや、あなたが夢や目標に誓いを立て、コミットしてきたことへの当然の結果なのです。\n「パーティーの計画を立てなさい。すぐに、その祝福の理由が分かります」","あなたは、偉大な発展と祝福の時期に入りました。あなたは、豊穣、祝福、歓待の季節にいざなわれています。今こそ、人生があなたにその実りで報いる時期なのです。あなたは婚約したり、結婚したり、昇格したり、何かを獲得したり、あるいは長く待たれたラッキーな休暇を得るかも知れません。\nあなたが何を望もうとも、確実にそれが来ているので準備をしましょう。人生の潮の流れがあなたの方へ向いてきており、それはあなたがしっかりと努力をしてきたことや、あなたが夢や目標に誓いを立て、コミットしてきたことへの当然の結果なのです。\n「パーティーの計画を立てなさい。すぐに、その祝福の理由が分かります」"]
    option_7 = ["あなたが結果を求めていることに関しては、もう少し時間が必要なようです。状況は悲観的ではありませんが、時間を必要としているのです。もともとこの道はゴールまでの道のりが果てしなく遠いものだったので、先々のことを考えたり先走ったりするのはあまり意味のないことでした。とは言え、結果は必ず出るよと告げられていますので、今は忍耐の時と割り切って、焦らず状況を楽しむくらいの感覚でいてください。芽が出たら花が咲く時が必ずやって来ます。","あなたは今、あなたの人間関係の中で、ギブ・アンド・テイクのバランスをいかにして保つかを学ぶ過程にいて、あなたのやり方を評価する時期です。あなたは与えすぎて、自分に憤りや怒りが残っていませんか？\nあるいは、もっと与えることが出来るのに掴んで離さず、自分はそのことに対して罪の意識や自己防衛の意識に悩まされていませんか？ギブ・アンド・テイクのレッスンは習得するのが一番難しい\n技能ではありますが、全ての人間関係において、いかに与え受け取るべきか、もっと気づくことが出来るようになりましょう。\n「愛を与えることと愛を受け取ることに違いはありません」","あなたは今、あなたの人間関係の中で、ギブ・アンド・テイクのバランスをいかにして保つかを学ぶ過程にいて、あなたのやり方を評価する時期です。あなたは与えすぎて、自分に憤りや怒りが残っていませんか？\nあるいは、もっと与えることが出来るのに掴んで離さず、自分はそのことに対して罪の意識や自己防衛の意識に悩まされていませんか？ギブ・アンド・テイクのレッスンは習得するのが一番難しい\n技能ではありますが、全ての人間関係において、いかに与え受け取るべきか、もっと気づくことが出来るようになりましょう。\n「愛を与えることと愛を受け取ることに違いはありません」"]
    option_8 = ["今の状態をあるがままに受け入れてください。抵抗せず、そのままを受け入れてください。どうしても認め難く変えたいと思うものは、一旦受け入れた後であなたの良いように変えてゆけばよいのです。状況はこれからとても良くなっていく可能性を秘めていますが、それはあなたの受容性の強化にかかっています。変化とはある程度の時間を要する事もありますから、タイミングが来るまでは意識的に「静かな受容」でいることに徹しましょう。","あなたは間違った選択か習慣的な行動のせいで、自分を自己批判し恥じ入る場面に遭遇するかも知れません。\nけれど、あなたは進化するためにここにいて、その道のりの中で多くの過ちも犯すでしょう。それはあなたの学習過程の一部であり、あなたの成長のために必要なことだという事を忘れないでください。\n結局のところ、とても深刻で重大であるがために、許しようがない過ちや失敗などないのです。周りの人たちも、たとえあなたがひどい過ちを犯しても、あなたを愛することを止めはしません。\n「生きて学びなさい」","あなたは間違った選択か習慣的な行動のせいで、自分を自己批判し恥じ入る場面に遭遇するかも知れません。\nけれど、あなたは進化するためにここにいて、その道のりの中で多くの過ちも犯すでしょう。それはあなたの学習過程の一部であり、あなたの成長のために必要なことだという事を忘れないでください。\n結局のところ、とても深刻で重大であるがために、許しようがない過ちや失敗などないのです。周りの人たちも、たとえあなたがひどい過ちを犯しても、あなたを愛することを止めはしません。\n「生きて学びなさい」"]
    option_9 = ["もしも今あなたが生き辛さや拘束感を感じて、息が詰まりそうな状態なら、それは自分で自分を縛っているからかも知れません。「９」のあなたは誠実で正直で、与えられたことは必ずやり遂げる意志の強さを持っています。けれどもあまりにも「こうあるべき」が強すぎてはいませんか？時には手抜きも息抜きも必要です。それは怠ける事ではなく、「建設的な柔軟さ」です。誰かの目や評価、ご機嫌など気にせず、あなたのやりやすい方法で生きてみてはいかがでしょうか♬","あなたが近頃何にも楽しみを感じられず、自分の歓びから切り離されていることについて治療をしましょう。\nリラックスして、楽しんで、楽しい時が流れるままにしてください。人生は楽しむもので、我慢するものではありません。美味しい食べ物や良い音楽、親しい友人、楽しい娯楽などであなたの魂を歓ばせてあげてください。自分を甘やかしすぎるとか、心を奪われる事に躊躇しないで。\n「どれだけ、この歓びに抵抗できますか？」","あなたが近頃何にも楽しみを感じられず、自分の歓びから切り離されていることについて治療をしましょう。\nリラックスして、楽しんで、楽しい時が流れるままにしてください。人生は楽しむもので、我慢するものではありません。美味しい食べ物や良い音楽、親しい友人、楽しい娯楽などであなたの魂を歓ばせてあげてください。自分を甘やかしすぎるとか、心を奪われる事に躊躇しないで。\n「どれだけ、この歓びに抵抗できますか？」"]

    #option = f"option_{result4}"
    shuffleInt = random.randint(0,2)
    allStr = [option_1,option_2,option_3,option_4,option_5,option_6,option_7,option_8,option_9]
    resultStr = allStr[result4 - 1][shuffleInt]
    line_bot_api.broadcast(TextSendMessage(text = resultStr))
    #line_bot_api.broadcast(TextSendMessage(text = random.choice(f"{option_{result4}}")))



if __name__ == "__main__":
    app.run()
