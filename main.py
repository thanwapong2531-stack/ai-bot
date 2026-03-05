from flask import Flask, request
import os

app = Flask(__name__)

# หน้าแรก (เอาไว้เช็คว่า server ทำงาน)
@app.route("/")
def home():
    return "AI LINE BOT RUNNING"

# webhook จาก LINE
@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_json()
    print(body)
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
