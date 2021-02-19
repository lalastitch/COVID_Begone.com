from flask import Flask, render_template, request, jsonify
import requests
from getCounty import get_county
from backend.zipcode import VaccinesZipcode, getItem

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/postmethod', methods=['POST'])
def postmethod():
    data = request.get_json()
    return get_county(data)


@app.route('/locations', methods=['POST'])
def locations():
    data = request.get_json()
    county = data["county"]
    return getItem(county)


if __name__ == "__main__":
    app.run(debug=True)
