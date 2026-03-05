from flask import Flask, request
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "ใส่ChannelAccessTokenตรงนี้"

@app.route("/")
def home():
    return "Bot is running"

@app.route("/callback", methods=["POST"])
def callback():
    body = request.json
    events = body.get("events", [])

    for event in events:
        if event["type"] == "message":
            replyToken = event["replyToken"]
            text = event["message"]["text"]

            reply(replyToken, "คุณพิมพ์ว่า: " + text)

    return "OK"

def reply(token, message):

    url = "https://api.line.me/v2/bot/message/reply"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
    }

    data = {
        "replyToken": token,
        "messages":[
            {
                "type":"text",
                "text":message
            }
        ]
    }

    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
