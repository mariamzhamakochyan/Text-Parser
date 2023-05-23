class Word:
    def __init__(self, word):
        self.word = word

    def clean_word(self):
        return ''.join(char for char in self.word if char.isalnum())

    def lowercase_word(self):
        return self.clean_word().lower()

    def normalize_word(self, dictionary):
        lowercase = self.lowercase_word()
        if lowercase in dictionary:
            return lowercase
        else:
            self.word = self.word.upper()