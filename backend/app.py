from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart Plant Disease Detector Running"

if __name__ == "__main__":
    app.run()
