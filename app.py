import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

# load environment parameter
load_dotenv()

# set FSM
machine = TocMachine(
    states=["user", "choose", "hulu", "Miaow", "ke", "ss", "ho", "ou", "y",
    "kitty1", "flighty1", "nervous1", "watch1", "act1", "enemy1", "new1", "threat1", "protect1", "bloom1",
    "kitty2", "flighty2", "nervous2", "enemy2", "new2"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "choose","conditions": "is_going_to_choose",},
        {"trigger": "advance","source": "choose","dest": "hulu","conditions": "is_going_to_hulu",},
        {"trigger": "advance","source": "choose","dest": "Miaow","conditions": "is_going_to_Miaow",},
        {"trigger": "advance","source": "choose","dest": "ke","conditions": "is_going_to_ke",},
        {"trigger": "advance","source": "choose","dest": "ss","conditions": "is_going_to_ss",},
        {"trigger": "advance","source": "choose","dest": "ho","conditions": "is_going_to_ho",},
        {"trigger": "advance","source": "choose","dest": "ou","conditions": "is_going_to_ou",},
        {"trigger": "advance","source": "choose","dest": "y","conditions": "is_going_to_y",},
        {"trigger": "advance","source": "hulu","dest": "kitty1","conditions": "is_going_to_kitty1",},
        {"trigger": "advance","source": "hulu","dest": "flighty1","conditions": "is_going_to_flighty1",},
        {"trigger": "advance","source": "hulu","dest": "nervous1","conditions": "is_going_to_nervous1",},
        {"trigger": "advance","source": "Miaow","dest": "watch1","conditions": "is_going_to_watch1",},
        {"trigger": "advance","source": "ke","dest": "act1","conditions": "is_going_to_act1",},
        {"trigger": "advance","source": "ss","dest": "enemy1","conditions": "is_going_to_enemy1",},
        {"trigger": "advance","source": "ss","dest": "new1","conditions": "is_going_to_new1",},
        {"trigger": "advance","source": "ho","dest": "threat1","conditions": "is_going_to_threat1",},
        {"trigger": "advance","source": "ou","dest": "protect1","conditions": "is_going_to_protect1",},
        {"trigger": "advance","source": "y","dest": "bloom1","conditions": "is_going_to_bloom1",},
        {"trigger": "advance","source": "kitty1","dest": "kitty2","conditions": "is_going_to_kitty2",},
        {"trigger": "advance","source": "flighty1","dest": "flighty2","conditions": "is_going_to_flighty2",},
        {"trigger": "advance","source": "nervous1","dest": "nervous2","conditions": "is_going_to_nervous2",},
        {"trigger": "advance","source": "enemy1","dest": "enemy2","conditions": "is_going_to_enemy2",},
        {"trigger": "advance","source": "new1","dest": "new2","conditions": "is_going_to_new2",},
        {"trigger": "go_back", "source": [ "hulu", "Miaow", "ke", "ss", "ho", "ou", "y", "watch1", "act1","threat1", "protect1", "bloom1","kitty2", "flighty2", "nervous2", "enemy2", "new2"], "dest": "user"},

    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# set line bot
# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

# create a new LineBotApi instance
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


# line bot route
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            # get reply_token from a webhook event object & send text
            send_text_message(event.reply_token, "請重新輸入~")

    return "OK"


# show fsm graph
@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ['PORT']
    app.run(host="0.0.0.0", port=port, debug=True)
