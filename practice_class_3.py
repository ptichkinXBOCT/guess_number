class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        index = None
        cipher_out = ''
        self.original_text = str.lower(original_text)
        self.shift = shift
        for letter in self.original_text:
            index = str.find(self.alphabet, letter)
            if index >= 0:
                cipher_out += self.alphabet[(index + self.shift) % 33]
            else:
                cipher_out += letter
        return cipher_out

    def decipher(self, cipher_text, shift):
        index = None
        decipher_out = ''
        self.cipher_text = str.lower(cipher_text)
        self.shift = shift
        for letter in self.cipher_text:
            index = str.find(self.alphabet, letter)
            if index >= 0:
                decipher_out += self.alphabet[(index - self.shift) % 33]
            else:
                decipher_out += letter
        return decipher_out

    def process_text(self, text, shift, is_encrypt):
        index = None
        text_out = ''
        self.text = str.lower(text)
        self.shift = shift
        self.is_encrypt = is_encrypt
        for letter in self.text:
            index = str.find(self.alphabet, letter)
            if (index >= 0 and is_encrypt):
                text_out += self.alphabet[(index + self.shift) % 33]
            elif (index >= 0 and not is_encrypt):
                text_out += self.alphabet[(index - self.shift) % 33]
            else:
                text_out += letter
        return text_out


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Пришло ревью в шифрованном виде. Кажется, нас расскрыли!',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))

cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
