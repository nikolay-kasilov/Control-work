"""
Придумать и написать шифровальщик текста
Он будет принимать строку и ключ шифрования, возвращать ее в зашифрованном виде
Затем должен быть дешифровальщик который пример зашифрованную строку и ключ и расшифрует ее
"""


"""Всем привет -> Жцйс фхнжй -> Всем привет"""  # Придумать что-то интереснее шифра Цезаря

encode_text ="".join(
    [
        (chr(ord(letter)+4))
        for letter in "Привет всем!"
    ]
)
decode_text = "".join(
    (chr(ord(letter)-4))
    for letter in encode_text
)
print(decode_text)
print(encode_text)

"""Всем привет -> Жцйс фхнжйч -> Всем привет"""  # Придумать что-то интереснее шифра Цезаря
encode_text ="".join(
    [
        (chr(ord(letter)+4))
        for letter in "Привет всем!"
    ]
)
decode_text = "".join(
    (chr(ord(letter)-4))
    for letter in encode_text
)
print(decode_text)
print(encode_text)

 

