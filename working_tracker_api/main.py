import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
YOUR_TOKEN = ""
GENDER = ""
WEIGHT = 0
HEIGHT = 0
AGE = 0

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = ""

exercise = input("What type of exercise? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(
    exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%Y%m%d")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": YOUR_TOKEN
    }
    sheet_response = requests.post(
        sheets_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response)
