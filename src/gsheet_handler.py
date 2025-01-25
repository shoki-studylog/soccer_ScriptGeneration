import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

#スクリプト実行ディレクトリによって、下記2行を追加する必要がある場合有（今回は、サブディレクトだからぽい？？）
import sys
sys.path.append("/Users/shoki/Desktop/youtubeShorts/ScriptGeneration_soccer")
from config.settings import GOOGLE_SHEET_URL


def get_keyword():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']  #OAuth認証を使用してアクセスできる範囲をスコープとして記載する。
    dir_path = os.path.dirname(os.path.realpath(__file__))  # 現在のファイルのディレクトリを取得
    creds_path = os.path.join(dir_path, '..', 'creds', 'credentials.json')  # 親ディレクトリに移動してから creds ディレクトリへ
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(GOOGLE_SHEET_URL).sheet1
    keyword = sheet.acell('A1').value
    return keyword

def write_to_sheet(title, content):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds/credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(GOOGLE_SHEET_URL).sheet1
    sheet.update('A2', title)
    sheet.update('B2', content)