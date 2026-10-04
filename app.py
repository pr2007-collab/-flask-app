from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1 style='text-align:center;margin-top:100px'>I love you - LIVE! Love GitHub: github.com/pr2007-collab/-flask-app</h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
