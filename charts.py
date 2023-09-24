import requests
import os
import json


CHARTS_FILE = "charts.json"
"""
CHARTS_DATABASE = []

if os.path.exists(CHARTS_FILE):
    with open(CHARTS_FILE, "r") as f:
        CHARTS_DATABASE = json.load(f)
"""


def get_access_token():
    url = "https://account.kkbox.com/oauth2/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": "180a8e56cbd3dd5b69e59b2f096cc690",
        "client_secret": "22b7fbc0442103cc8ccc70a0f9f8f51b"
    }

    access_token = requests.post(url, headers=headers, data=data)
    return access_token.json()["access_token"]


def get_charts_tracks(chart_id):
    access_token = get_access_token()
    # print(access_token)
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }

    params = {
        "territory": "TW"
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]

    for item in result:
        print(item["name"], item["url"])

    return result


def get_charts():
    access_token = get_access_token()
    # print(access_token)
    url = "https://api.kkbox.com/v1.1/charts"

    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }

    params = {
        "territory": "TW"
    }

    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)
    assert response.status_code == 200
    result = response.json()["data"]
    # result = response.json()
    # print(result)

    with open(CHARTS_FILE, "w") as f:
        json.dump(result, f)

    for item in result:
        print(item["id"], item["title"])


while True:
    try:
        chart_id = input("請貼上想聽的音樂排行榜ID: ")
        get_charts_tracks(chart_id)
        break

    except KeyError:
        print("請貼上正確的音樂排行榜ID")
