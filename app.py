from flask import Flask, request, abort

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
    reply = '抱歉我還沒做好這部分'

    if msg = '生日卡片':
        reply = '...'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()