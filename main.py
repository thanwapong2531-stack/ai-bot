from flask import Flask, request
import requests

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "RmtuiUMHvINlgkwBsjuntE38WR5VJzbgqz5tFkzMG4ADol3k4soTh0TnPrJXYKKrp+qdSqVorvvtA00rFlbXa5dCuKdIy5YDPGlIHCgTQc/oCKpMc35n1kVfNW7BM3HjGXDKMszka1g4Yqcq2GOUhwdB04t89/1O/w1cDnyilFU="

@app.route("/callback", methods=["POST"])
def callback():
    data = request.json

    for event in data["events"]:
        replyToken = event["replyToken"]
        text = event["message"]["text"]

        url = "https://api.line.me/v2/bot/message/reply"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
        }

        body = {
            "replyToken": replyToken,
            "messages":[
                {
                    "type":"text",
                    "text":"คุณพิมพ์ว่า: " + text
                }
            ]
        }

        requests.post(url, headers=headers, json=body)

    return "OK"

@app.route("/")
def home():
    return "Bot running"
