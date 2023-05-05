import requests
import json

chatGPTApiKey = "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"

textInput = input('Enter Some Text: ')

requestHeaders = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

requestData = {
    'prompt': textInput,
    'max_tokens': 100,
    'temperature': 0.5,
}

response = requests.post(
    'https://api.openai.com/v1/engines/text-davinci-003/completions',
    headers = requestHeaders,
    json = requestData
)

if response.status_code == 200:
    responseData = json.loads(response.text)
    print(responseData['choices'][0]['text'])
else:
    print(f'Error: {str(response.status_code)}')