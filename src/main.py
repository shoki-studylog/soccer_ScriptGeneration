# from gsheet_handler import get_keyword, write_to_sheet
# from trivia_generator import generate_trivia
# from translator import translate_text
# from line_notifier import send_line_notification
from gsheet_handler import get_keyword

def main():
    keyword = get_keyword()
    # title, content = generate_trivia(keyword)
    # title_ja = translate_text(title)
    # content_ja = translate_text(content)
    # write_to_sheet(title_ja, content_ja)
    # send_line_notification("処理が完了しました。詳細はスプレッドシートをご覧ください。")

if __name__ == "__main__":
    main()