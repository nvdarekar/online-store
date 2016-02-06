from flask import (Flask, request, render_template, jsonify)

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(threaded=True , debug=True)
    #app.run(threaded=True)
