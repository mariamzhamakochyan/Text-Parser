from src.word import Word
from src.text import Text

def parse_files():
    files = ["resources/1.txt", "resources/2.txt"]
    word_dict = {}

    for file_name in files:
        with open(file_name, "r") as file:
            content = file.read().split()
            for word in content:
                word_obj = Word(word)
                lowercase_word = word_obj.lowercase_word()
                if lowercase_word in word_dict:
                    if file_name not in word_dict[lowercase_word]:
                        word_dict[lowercase_word].append(file_name)
                else:
                    word_dict[lowercase_word] = [file_name]

    with open("db.txt", "w") as output_file:
        for word, file_list in word_dict.items():
            file_numbers = ','.join(file_list)
            output_file.write(f"{word}:{file_numbers}\n")


def search_word(keyword):
    with open("db.txt", "r") as db_file:
        for line in db_file:
            word, files = line.strip().split(':')
            if word == keyword:
                return files.split(',')
    return []



