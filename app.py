from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Must be Identical on the Air Quality Monitor
AQM_API_KEY = "C7r57niMC6PFQXebcymAFLCdGGRRNGyM"

# Routes
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route("/get_json/data", methods=['GET','POST'])
def get_json():
    client_key = request.headers.get("AQM-API-KEY") # Ensure that the API key is the same

    # Check if client is the air quality monitor
    if not client_key or client_key != AQM_API_KEY:
        print("Imposter! Not my Air Quality Monitor!")
        return jsonify({"status": "error", "message": "Unauthorized"}), 401 # Unauthorize Response
    
    # Check if package is a json file
    if request.is_json:
        data = request.get_json() # Get JSON file from ESP32
        print("Data is a JSON package")
        return jsonify({"status": "success", "message": "data received"}), 200 # Success Response
    else:
        print("data is not a JSON package")
        return jsonify({"status": "error", "message": "Not JSON Package"}), 400 # Error Response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)