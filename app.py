import json
import requests
from string import Template

API_URL = "https://api-inference.huggingface.co/models/mio/Artoria"
headers = {"Authorization": "Bearer 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"}

cnapi = Template("https://genshin.azurewebsites.net/api/speak?format=mp3&text=${24}&id=${1}")

api = "https://genshin.azurewebsites.net/api/speak?format=mp3&text=24id=1"

def query(payload):
	response = requests.post(api)
	return response.json()
	
output = query({
	"inputs": "The answer to the universe is 42",
})

print(output)