from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('tQebfBnwE0RW1R/5vVOCzTAJtAIZbZ3hAvXT4MttVwofVz33/m/a64N6ya87ldYTP+CL4LjVQIcymWv+rhuskNyND0oq+eNZfWOkCdoR+v+2xLPXc1NiKNFPqADWVj277L+nqBneBPlHihU7EFaH9AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1ed93a769d65b1ddd7fcbfbe75a7733c')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = '抱歉我還沒做好這部分，歡迎跟白鈞元說。'
    

    if msg == '生日卡片':
        reply = '我的小餛飩王子瑄寶貝22歲生日快樂!!!今年真是辛苦你了，遇到了好多事情，你每次都跟我說覺得我很辛苦要一直照顧你甚麼的，但其實你自己也幫了我很多忙，像是教程的課還有教學實習的部分，那些沒有你我是絕對不知道要怎麼辦，而且你也時常在生活中聽我抱怨事情、也會在我心情不好的時候安慰我聽我說，所以不要太自責或給自己太大的壓力，不用想著要自己快點好起來，這種事情不是你自己能控制的，平常日上課的時候就由我來陪著你，假日的時候就回桃園好好休息、好好運動。最困難的21歲跟2020都一起過去了，新的一年我會繼續陪著你，一切一定會越來越好的，我相信你!你也要相信自己! 最後不用特別祝福甚麼，只祝福你在新的一年可以好好生活、好好吃飯、好好睡覺、我們繼續好好在一起<3'        

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply), StickerSendMessage(package_id='3', sticker_id='257'))



if __name__ == "__main__":
    app.run()