from flask import Flask

app = Flask(__name__) # Init Server

#routes
@app.route("/")
def index():
    return "WHAT"

app.run(host="0.0.0.0", port=50100, debug=True, ssl_context="adhoc")