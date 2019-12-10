import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "picture","west_team","east_team","northwest_divition","pacific_divition","southwest_divition","atalantic_divition","central_divition","southeast_divition","jazz","nuggets","thunders","timberwolves","trail_blazers","clippers","kings","lakers","suns","warriors","mavericks","grizzles","pelicans","rockets","spurs","raptors","celtics","76ers","nets","knics","bucks","pacers","pistons","bulls","caveliers","heats","magic","hornets","wizards","hawks","highlight"],
    transitions=[
        {#user->picture
            "trigger": "advance",
            "source": "user",
            "dest": "picture",
            "conditions": "is_going_to_picture",
        },
        {#picture->west_team
            "trigger": "advance",
            "source": "picture",
            "dest": "west_team",
            "conditions": "is_going_to_west_team",
        },
        {#west_team->northwest_divition
            "trigger": "advance",
            "source": "west_team",
            "dest": "northwest_divition",
            "conditions": "is_going_to_northwest_divition",
        },
        {#northwest_divition->jazz
            "trigger": "advance",
            "source": "northwest_divition",
            "dest": "jazz",
            "conditions": "is_going_to_jazz",
        },
        {#northwest_divition->nuggets
            "trigger": "advance",
            "source": "northwest_divition",
            "dest": "nuggets",
            "conditions": "is_going_to_nuggets",
        },
        {#northwest_divition->thunders
            "trigger": "advance",
            "source": "northwest_divition",
            "dest": "thunders",
            "conditions": "is_going_to_thunders",
        },
        {#northwest_divition->timberwolves
            "trigger": "advance",
            "source": "northwest_divition",
            "dest": "timberwolves",
            "conditions": "is_going_to_timberwolves",
        },
        {#northwest_divition->trail_blazers
            "trigger": "advance",
            "source": "northwest_divition",
            "dest": "trail_blazers",
            "conditions": "is_going_to_trail_blazers",
        },
        {#west_team->pacific_divition
            "trigger": "advance",
            "source": "west_team",
            "dest": "pacific_divition",
            "conditions": "is_going_to_pacific_divition",
        },
        {#pacific_divition->clippers
            "trigger": "advance",
            "source": "pacific_divition",
            "dest": "clippers",
            "conditions": "is_going_to_clippers",
        },
        {#pacific_divition->kings
            "trigger": "advance",
            "source": "pacific_divition",
            "dest": "kings",
            "conditions": "is_going_to_kings",
        },
        {#pacific_divition->lakers
            "trigger": "advance",
            "source": "pacific_divition",
            "dest": "lakers",
            "conditions": "is_going_to_lakers",
        },
        {#pacific_divition->suns
            "trigger": "advance",
            "source": "pacific_divition",
            "dest": "suns",
            "conditions": "is_going_to_suns",
        },
        {#pacific_divition->warriors
            "trigger": "advance",
            "source": "pacific_divition",
            "dest": "warriors",
            "conditions": "is_going_to_warriors",
        },
        {#west_team->southeast_divition
            "trigger": "advance",
            "source": "west_team",
            "dest": "southwest_divition",
            "conditions": "is_going_to_southwest_divition",
        },
        {#southwest_divition->mavericks
            "trigger": "advance",
            "source": "southwest_divition",
            "dest": "mavericks",
            "conditions": "is_going_to_mavericks",
        },
        {#southwest_divition->grizzles
            "trigger": "advance",
            "source": "southwest_divition",
            "dest": "grizzles",
            "conditions": "is_going_to_grizzles",
        },
        {#southwest_divition->pelicans
            "trigger": "advance",
            "source": "southwest_divition",
            "dest": "pelicans",
            "conditions": "is_going_to_pelicans",
        },
        {#southwest_divition->rockets
            "trigger": "advance",
            "source": "southwest_divition",
            "dest": "rockets",
            "conditions": "is_going_to_rockets",
        },
        {#southwest_divition->spurs
            "trigger": "advance",
            "source": "southwest_divition",
            "dest": "spurs",
            "conditions": "is_going_to_spurs",
        },
        {#picture->east_team
            "trigger": "advance",
            "source": "picture",
            "dest": "east_team",
            "conditions": "is_going_to_east_team",
        },
        {#east_team->atalantic_divition
            "trigger": "advance",
            "source": "east_team",
            "dest": "atalantic_divition",
            "conditions": "is_going_to_atalantic_divition",
        },
        {#atalantic_divition->raptors
            "trigger": "advance",
            "source": "atalantic_divition",
            "dest": "raptors",
            "conditions": "is_going_to_raptors",
        },
        {#atalantic_divition->celtics
            "trigger": "advance",
            "source": "atalantic_divition",
            "dest": "celtics",
            "conditions": "is_going_to_celtics",
        },
        {#atalantic_divition->76ers
            "trigger": "advance",
            "source": "atalantic_divition",
            "dest": "76ers",
            "conditions": "is_going_to_76ers",
        },
        {#atalantic_divition->nets
            "trigger": "advance",
            "source": "atalantic_divition",
            "dest": "nets",
            "conditions": "is_going_to_nets",
        },
        {#atalantic_divition->knics
            "trigger": "advance",
            "source": "atalantic_divition",
            "dest": "knics",
            "conditions": "is_going_to_knics",
        },
        {#east_team->central_divition
            "trigger": "advance",
            "source": "east_team",
            "dest": "central_divition",
            "conditions": "is_going_to_central_divition",
        },
        {#central_divition->bucks
            "trigger": "advance",
            "source": "central_divition",
            "dest": "bucks",
            "conditions": "is_going_to_bucks",
        },
        {#central_divition->pacers
            "trigger": "advance",
            "source": "central_divition",
            "dest": "pacers",
            "conditions": "is_going_to_pacers",
        },
        {#central_divition->pistons
            "trigger": "advance",
            "source": "central_divition",
            "dest": "pistons",
            "conditions": "is_going_to_pistons",
        },
        {#central_divition->bulls
            "trigger": "advance",
            "source": "central_divition",
            "dest": "bulls",
            "conditions": "is_going_to_bulls",
        },
        {#central_divition->caveliers
            "trigger": "advance",
            "source": "central_divition",
            "dest": "caveliers",
            "conditions": "is_going_to_caveliers",
        },
        {#east_team->southeast_divition
            "trigger": "advance",
            "source": "east_team",
            "dest": "southeast_divition",
            "conditions": "is_going_to_southeast_divition",
        },
        {#southeast_divition->heats
            "trigger": "advance",
            "source": "southeast_divition",
            "dest": "heats",
            "conditions": "is_going_to_heats",
        },
        {#southeast_divition->magic
            "trigger": "advance",
            "source": "southeast_divition",
            "dest": "magic",
            "conditions": "is_going_to_magic",
        },
        {#southeast_divition->hornets
            "trigger": "advance",
            "source": "southeast_divition",
            "dest": "hornets",
            "conditions": "is_going_to_hornets",
        },
        {#southeast_divition->wizards
            "trigger": "advance",
            "source": "southeast_divition",
            "dest": "wizards",
            "conditions": "is_going_to_wizards",
        },
        {#southeast_divition->hawks
            "trigger": "advance",
            "source": "southeast_divition",
            "dest": "hawks",
            "conditions": "is_going_to_hawks",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "highlight",
            "conditions": "is_going_to_highlight",
        },
        {
            "trigger": "advance", 
            "source": ["user", "team","west_team","east_team","northwest_divition","pacific_divition","souththwest_divition","atalantic_divition","central_divition","southeast_divition","jazz","nuggets","thunders","timberwolves","trail_blazers","clippers","kings","lakers","suns","warriors","mavericks","grizzles","pelicans","rockets","spurs","raptors","celtics","76ers","nets","knics","bucks","pacers","pistons","bulls","caveliers","heats","magic","hornets","wizards","hawks"], 
            "dest": "user",
            "conditions": "restart",
        },
        {"trigger": "go_back", "source": "highlight", "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


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
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
