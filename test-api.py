import requests
from dotenv import load_dotenv
import os

load_dotenv()
question = 'where is the capital of USA?'
question = 'where is the capital of Canada?'

url = 'http://localhost:8000/generate?prompt=' + question
headers = {'x-api-key': os.getenv('API_KEY'), 'Content-Type': 'application/json'}

response = requests.post(url, headers = headers)

if response.status_code == 200 :
  print(response.json()['response'])
else :
  print(response.status_code)
  print(response.json()['detail'])
