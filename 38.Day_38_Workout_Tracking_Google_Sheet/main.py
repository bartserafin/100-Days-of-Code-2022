from config import *
import requests
from datetime import datetime as dt

# Nutrition API
nutrition_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

GENDER = 'male'
WEIGHT_KG = 87
HEIGHT_CM = 188
AGE = 27

exercise_text = input('Exercises completed:')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

# POST a new exercise into a sheet
response = requests.post(nutrition_exercise_endpoint, json=params, headers=headers)
print(response)
result = response.json()
print(result)

# Sheet API and Google Sheets
sheet_post_endpoint = 'https://api.sheety.co/9d27c81f3e1e14dc091b8e762f4ef65d/myWorkouts/workouts'
today = dt.now().strftime('%d/%m/%Y')
now_time = dt.now().strftime('%X')

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': today,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    # POST the username and password for Basic Authentication
    sheet_response = requests.post(
        sheet_post_endpoint,
        json=sheet_input,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )
    print(sheet_response.text)
