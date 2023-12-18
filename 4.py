"""
Придумать и написать шифровальщик текста
Он будет принимать строку и ключ шифрования, возвращать ее в зашифрованном виде
Затем должен быть дешифровальщик который пример зашифрованную строку и ключ и расшифрует ее
"""

"""Всем привет -> Жцйс фхнжйч -> Всем привет"""  # Придумать что-то интереснее шифра Цезаря


def encrypt_text(text: str, key: dict) -> str:
    """
    Шифрует текст с использованием алгоритма полиалфавитной замены.

    text: Исходная строка для шифрования
    key: Словарь, представляющий ключ шифрования (пример: {'а': 'г', 'б': 'д', ...})
    return: Зашифрованная строка
    """
    encrypted_text = ""
    for char in text:
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text


def decrypt_text(text: str, key: dict) -> str:
    """
    Расшифровывает текст, зашифрованный с использованием алгоритма полиалфавитной замены.

    text: Зашифрованная строка
    key: Словарь, представляющий ключ шифрования
    return: Расшифрованная строка
    """
    decrypted_text = ""
    reversed_key = {v: k for k, v in key.items()}
    for char in text:
        if char in reversed_key:
            decrypted_text += reversed_key[char]
        else:
            decrypted_text += char
    return decrypted_text


# Пример использования
original_message = "я сделал контрольную"
encryption_key = {'п': 'т', 'р': 'у', 'и': 'ф', 'в': 'ж', 'е': 'з', 'т': 'ю', ' ': ' '}  # Пример ключа шифрования

encrypted_message = encrypt_text(original_message, encryption_key)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = decrypt_text(encrypted_message, encryption_key)
print("Расшифрованное сообщение:", decrypted_message)