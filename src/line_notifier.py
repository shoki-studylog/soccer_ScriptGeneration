# src/line_notifier.py
import requests
from config.settings import LINE_TOKEN

def send_line_notification(message):
    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': f'Bearer {LINE_TOKEN}'}
    data = {'message': message}
    response = requests.post(url, headers=headers, data=data)
    return response.status_code