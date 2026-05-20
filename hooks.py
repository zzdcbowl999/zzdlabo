import re

def on_page_markdown(markdown, page, config, files):
    
    def convert_ruby_tags(text):
        # 修正した正規表現パターン:
        # \|          : 縦棒「|」をエスケープして一致させる
        # ([^|《\n]+) : 「|」「《」「改行」以外の文字列（親文字）
        # 《([^》\n]+)》: 「》」「改行」以外の文字列（ルビ）
        pattern = r'\|([^|《\n]+)《([^》\n]+)》'
        
        # \1 に親文字、\2 にルビが入るようにHTMLタグへ置換
        result = re.sub(pattern, r'<ruby>\1<rt>\2</rt></ruby>', text)
        
        return result

    """
    MkDocs標準のフック機能。MarkdownがHTMLに変換される前に自動で実行されます。
    """
    return convert_ruby_tags(markdown)