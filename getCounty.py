import requests
import json


def get_county(jsonData):
    input = jsonData
    latitude = input["latitude"]
    longitude = input["longitude"]
    response = requests.get(
        "https://geo.fcc.gov/api/census/area?lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json")

    if (response.status_code == 200):
        json_file = response.json()["results"][0]
        return json.dumps({"county_name": json_file["county_name"]})


if __name__ == "__main__":
    get_county(37.774929, -122.419418)
