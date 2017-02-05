#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(text):
    """与えられた文の各文字を，以下の仕様で変換する関数

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力
    """
    cipher_text = ""
    for char in text:
        if char.islower():
            cipher_text += chr(219 - ord(char))
        else:
            cipher_text += char
    return cipher_text

# 英語のメッセージを暗号化・復号化
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine."
print("origin text : " + text)
cipher_text = cipher(text)
print("cipher text : " + cipher_text)
decode_text = cipher(cipher_text)
print("decode text : " + decode_text)
