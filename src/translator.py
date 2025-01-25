import requests
from config.settings import TRANSLATE_API_KEY

def translate_text(text, source_lang='en', target_lang='ja'):
    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
    headers = {
        'Ocp-Apim-Subscription-Key': TRANSLATE_API_KEY,
        'Content-type': 'application/json',
        'Ocp-Apim-Subscription-Region': 'global',
    }
    body = [{'text': text}]
    params = {'from': source_lang, 'to': target_lang}
    response = requests.post(url, params=params, headers=headers, json=body)
    result = response.json()
    return result[0]['translations'][0]['text']