from src.word import Word
from src.text import Text

def word_db():
    files = ["resources/1.txt", "resources/2.txt"]
    word_dict = {}

    for file_ in files:
        with open(file_, "r") as file:
            content = file.read().split()
            for word in content:
                word_ = Word(word)
                lowercase_word = word_.lowercase_word()
                if lowercase_word in word_dict:
                    if file_ not in word_dict[lowercase_word]:
                        word_dict[lowercase_word].append(file_)
                else:
                    word_dict[lowercase_word] = [file_]

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


word_db()
while True:
    keyword = input("Enter a word to search, or press 'Enter' to quit: ")
    if keyword == "":
        break
    search_result = search_word(keyword)
    if search_result:
        print(f"The word '{keyword}' is found in files: {', '.join(search_result)}")
    else:
        print(f"The word '{keyword}' is not found.")
