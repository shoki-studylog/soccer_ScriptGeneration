import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import GOOGLE_SHEET_URL

def get_keyword():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds/credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(GOOGLE_SHEET_URL).sheet1
    keyword = sheet.acell('A1').value
    return keyword

def write_to_sheet(title, content):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds/credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(GOOGLE_SHEET_URL).sheet1
    sheet.update('A2', title)
    sheet.update('B2', content)