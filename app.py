from flask import Flask, jsonify, request

app = Flask(__name__)

# Routes
@app.route('/')
def dashboard():
    

@app.route("/get_json/data", methods=['POST'])
def get_json():
    if request.is_json:
        data = request.get_json() # Get JSON file from ESP32
        return 200 # Success Response
    else:
        return 400 # Error Response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)