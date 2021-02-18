import requests

def get_county
response = requests.get(
    "https://geo.fcc.gov/api/census/area?lat=37.774929&lon=-122.419418&format=json")
