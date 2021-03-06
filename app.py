import random

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
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
    
    if '功能' in msg:
        reply = '1.生日卡片\n2.北極熊(後面加上編號1到5的話可以指定)\n3.弟弟(後面加上編號1到7的話可以指定)'
    elif msg == '生日卡片':
        reply = '我的小餛飩王子瑄寶貝22歲生日快樂!!!\n今年真是辛苦你了，遇到了好多事情，你每次都跟我說覺得我很辛苦要一直照顧你甚麼的，但其實你自己也幫了我很多忙，像是教程的課還有教學實習的部分，那些沒有你我是絕對不知道要怎麼辦，而且你也時常在生活中聽我抱怨事情、也會在我心情不好的時候安慰我聽我說，所以不要太自責或給自己太大的壓力，不用想著要自己快點好起來，這種事情不是你自己能控制的，平常日上課的時候就由我來陪著你，假日的時候就回桃園好好休息、好好運動。\n最困難的21歲跟2020都一起過去了，新的一年我會繼續陪著你，一切一定會越來越好的，我相信你!你也要相信自己! 最後不用特別祝福甚麼，只祝福你在新的一年可以好好生活、好好吃飯、好好睡覺、我們繼續好好在一起<3'        

    #北極熊
    if msg == '北極熊':
        url = ['https://s.yimg.com/ny/api/res/1.2/3QLYhau.SJMgY7YyRn9TFw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwMDA7aD0xMzMz/https://s.yimg.com/os/creatr-uploaded-images/2020-10/42c22820-1821-11eb-97fe-a8b44e98b81c', 'https://hk.appledaily.com/resizer/bOSC4LbLyBaDCl5ctgmWU40hGik=/720x0/filters:quality(100)/cloudfront-ap-northeast-1.images.arcpublishing.com/appledaily/TWANNPPS45BA3NOQT5VX3OVGUE.jpg', 'https://n.sinaimg.cn/spider2020227/533/w800h533/20200227/8f38-ipzreiw8266715.jpg', 'https://petsmao-media.nownews.com/images/2019/12/372887e9-1576832623-de044bf41be1645832b20120e2efb02f.jpg', 'https://img.natgeomedia.com/userfiles/sm/sm1920_images_A1/4737/10104810726108.jpg']
        picurl = url[random.randint(0, 4)]
        previewpicurl = picurl
        image_message = ImageSendMessage(
            original_content_url=picurl,
            preview_image_url=previewpicurl
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '北極熊1':

        image_message = ImageSendMessage(
            original_content_url='https://s.yimg.com/ny/api/res/1.2/3QLYhau.SJMgY7YyRn9TFw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwMDA7aD0xMzMz/https://s.yimg.com/os/creatr-uploaded-images/2020-10/42c22820-1821-11eb-97fe-a8b44e98b81c',
            preview_image_url='https://s.yimg.com/ny/api/res/1.2/3QLYhau.SJMgY7YyRn9TFw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTIwMDA7aD0xMzMz/https://s.yimg.com/os/creatr-uploaded-images/2020-10/42c22820-1821-11eb-97fe-a8b44e98b81c'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '北極熊2':
        image_message = ImageSendMessage(
            original_content_url='https://hk.appledaily.com/resizer/bOSC4LbLyBaDCl5ctgmWU40hGik=/720x0/filters:quality(100)/cloudfront-ap-northeast-1.images.arcpublishing.com/appledaily/TWANNPPS45BA3NOQT5VX3OVGUE.jpg',
            preview_image_url='https://hk.appledaily.com/resizer/bOSC4LbLyBaDCl5ctgmWU40hGik=/720x0/filters:quality(100)/cloudfront-ap-northeast-1.images.arcpublishing.com/appledaily/TWANNPPS45BA3NOQT5VX3OVGUE.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '北極熊3':
        image_message = ImageSendMessage(
            original_content_url='https://n.sinaimg.cn/spider2020227/533/w800h533/20200227/8f38-ipzreiw8266715.jpg',
            preview_image_url='https://n.sinaimg.cn/spider2020227/533/w800h533/20200227/8f38-ipzreiw8266715.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '北極熊4':
        image_message = ImageSendMessage(
            original_content_url='https://petsmao-media.nownews.com/images/2019/12/372887e9-1576832623-de044bf41be1645832b20120e2efb02f.jpg',
            preview_image_url='https://petsmao-media.nownews.com/images/2019/12/372887e9-1576832623-de044bf41be1645832b20120e2efb02f.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '北極熊5':
        image_message = ImageSendMessage(
            original_content_url='https://img.natgeomedia.com/userfiles/sm/sm1920_images_A1/4737/10104810726108.jpg',
            preview_image_url='https://img.natgeomedia.com/userfiles/sm/sm1920_images_A1/4737/10104810726108.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)

    #弟弟
    if msg == '弟弟':
        url = ['https://i.imgur.com/sEMpJh5.jpg', 'https://i.imgur.com/IK5LByI.jpg', 'https://i.imgur.com/ETxGvls.jpg', 'https://i.imgur.com/PHSKD4c.jpg', 'https://i.imgur.com/yMxOzRw.jpg', 'https://i.imgur.com/LcuxZbu.jpg', 'https://i.imgur.com/B1zptQq.jpg']
        picurl = url[random.randint(0, 6)]
        previewpicurl = picurl
        image_message = ImageSendMessage(
            original_content_url=picurl,
            preview_image_url=previewpicurl
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟1':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/sEMpJh5.jpg',
            preview_image_url='https://i.imgur.com/sEMpJh5.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟2':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/IK5LByI.jpg',
            preview_image_url='https://i.imgur.com/IK5LByI.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟3':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ETxGvls.jpg',
            preview_image_url='https://i.imgur.com/ETxGvls.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟4':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/PHSKD4c.jpg',
            preview_image_url='https://i.imgur.com/PHSKD4c.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟5':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/yMxOzRw.jpg',
            preview_image_url='https://i.imgur.com/yMxOzRw.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟6':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/LcuxZbu.jpg',
            preview_image_url='https://i.imgur.com/LcuxZbu.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)
    elif msg == '弟弟7':

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/B1zptQq.jpg',
            preview_image_url='https://i.imgur.com/B1zptQq.jpg'
        )

        line_bot_api.reply_message(
        event.reply_token,
        image_message)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))



if __name__ == "__main__":
    app.run()