from flask import Flask,request, abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMseeage

import bot_info
app = Flask(__name__)
line_bot_api = LineBotApi(bot_info.line_bot_token)
handler = WebhookHandler(bot_info,line_bot_secert)

@app.route('/callback',methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Reequest body:' + body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@handler.add(MessagwEvent,message =TextMessage)
def echo(event):
    message = TextSendMseeade(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
if __name__ == '__main__':
    app.run()