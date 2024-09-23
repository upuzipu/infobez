from model.affine import аffine_сipher

if __name__ == '__main__':
    with open("encrypted_text.txt", 'r', encoding='utf-8') as file:
        encr_text = file.read()
    affine = аffine_сipher('keywords')
    text = encr_text
    a = 15
    b = 4
    encrypt_text = affine.encrypt(text, a, b)
    print(f"Encrypt word = {encrypt_text}")
    decrypt_text = affine.decrypt(encrypt_text, a, b)
    print(f"Decrypt word = {decrypt_text}")
    frequency_analysis = affine.analyze_frequency(encrypt_text)
    print("Частотный анализ:")
    for char, freq in affine.analyze_frequency(encrypt_text).items():
        print(f"{char}: {freq // 2}")
    print("\n")
    affine.check_keywords(encrypt_text)
    print("\nТоп 10 наиболее часто встречающихся слов:")
    top_words = affine.get_top_n_words(encrypt_text)
    for word, freq in top_words:
        print(f"{word}: {freq}")
