import re

from lab1.helpers import is_relatively_prime
from collections import Counter
from lab1.helpers import load_keyword_list


class аffine_сipher:
    """
    Класс который реализует афинный шифр
    """

    def __init__(self, keyword_list_path):
        """
        Init метод
        :param keyword_list_path: Путь до массива с ключевыми словами
        """
        self.keyword_list = load_keyword_list(keyword_list_path)
        self.frequency_analysis = Counter()
        self.ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.en = 'abcdefghijklmnopqrstuvwxyz'
        self.answer = ''

    def encrypt(self, text, a, b):
        """
        Шифрование текста афинным методом
        :param text: Текст для кодировки
        :param a: Параметр а из формулы кодирования
        :param b: Параметр b из формулы кодирования
        :return: Зашифрованный текст
        """
        self.answer = ''
        index = 0
        for letter in text:
            letter_status = False
            if letter.lower() in self.ru:
                if not is_relatively_prime(len(self.ru), a):
                    return "Русский алфавит и число a взаимно простые"
                if letter not in self.ru:
                    letter_status = True
                new_letter = self.ru[(a * self.ru.index(letter.lower()) + b) % len(self.ru)]
                if letter_status:
                    self.answer += new_letter.upper()
                else:
                    self.answer += new_letter
            elif letter.lower() in self.en:
                if not is_relatively_prime(len(self.en), a):
                    return "Английский алфавит и число a взаимно простые"
                if letter not in self.en:
                    letter_status = True
                new_letter = self.en[(a * self.en.index(letter.lower()) + b) % len(self.en)]
                if letter_status:
                    self.answer += new_letter.upper()
                else:
                    self.answer += new_letter
            else:
                self.answer += letter
            index += 1
        return self.answer

    def decrypt(self, text, a, b):
        """
        Расшифровка текста афинным методом
        :param text: Зашифрованный текст
        :param a: Изначальный параметр а для формулы
        :param b: Изначальный параметр b для формулы
        :return: Расшифрованный текст
        """
        self.answer = ''
        index = 0
        for letter in text:
            letter_status = False
            if letter.lower() in self.ru:
                a_ru = pow(a, -1, len(self.ru))
                if not is_relatively_prime(len(self.ru), a):
                    return "Русский алфавит и число a взаимно простые"
                if letter not in self.ru:
                    letter_status = True
                new_letter = self.ru[(a_ru * self.ru.index(letter.lower()) + b) % len(self.ru)]
                if letter_status:
                    self.answer += new_letter.upper()
                else:
                    self.answer += new_letter
            elif letter.lower() in self.en:
                a_en = pow(a, -1, len(self.en))
                if not is_relatively_prime(len(self.en), a):
                    return "Английский алфавит и число a взаимно простые"
                if letter not in self.en:
                    letter_status = True
                new_letter = self.en[(a_en * (self.en.index(letter.lower()) - b)) % len(self.en)]
                if letter_status:
                    self.answer += new_letter.upper()
                else:
                    self.answer += new_letter
            else:
                self.answer += letter
            index += 1
        return self.answer

    def analyze_frequency(self, encrypted_text):
        """
        Частотый анализ символов в тексте
        :param encrypted_text: Зашифрованный текст
        :return: Словарь с символом и их количеством в тексте
        """
        for char in encrypted_text:
            self.frequency_analysis[char] += 1
        return dict(self.frequency_analysis)

    def check_keywords(self, encrypted_text):
        """
        Метод для проверки наличия ключевых слов в тексте
        :param encrypted_text: Зашифрованный текст
        """
        for keyword in self.keyword_list:
            if keyword in encrypted_text:
                pattern = rf'\b{keyword}\b'
                print(f"Ключевое слово {keyword} встречается {len(re.findall(pattern, encrypted_text))} раз")
            else:
                print(f"Ключевое слово '{keyword}' не найдено в зашифрованном тексте.")

    def get_top_n_words(self, encrypted_text, n=10):
        """
        Метод для вывода 10 самых частых слов в тексте
        :param encrypted_text: Зашифрованный текст
        :param n: Изначально задано 10 - количество слов
        :return: Массив со словами
        """
        word_freq = Counter(re.findall(r'\b[a-zA-Zа-яА-Я]{2,}\b', encrypted_text))
        return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:n]
