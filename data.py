import requests
from dotenv import load_dotenv
import os

load_dotenv()

params = {
    "amount": 10,
    "type": "boolean"
}

res = requests.get(url=os.getenv("QUIZ_API_URL_BASE"), params=params)
res.raise_for_status()

question_data = res.json()["results"]
