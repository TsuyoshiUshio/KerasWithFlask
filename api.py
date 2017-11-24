from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/construction/v1/image/analize")
def analyze_image():
    picture = request.args.get("picture")
    return picture + " are sucks!"

if __name__ == "__main__":
    app.run()
