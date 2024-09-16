import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = re.sub(r'[,\.\=\!\?\;\:\-]', '', text)
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            position = words.index(word.lower())
            result[file_name] = position + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('text'))
print(finder.count('text'))
