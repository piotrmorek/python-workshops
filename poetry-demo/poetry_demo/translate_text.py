import json
import os
from typing import List

class WordCollection:
    words: List[str]
    lang: str = 'en'

    def __init__(self, words: List[str], lang: str):
        self.words = words
        self.lang = lang

    def __str__(self):
        return f'{self.words}'

    @classmethod
    def from_json(cls, filename) -> 'WordCollection':
        data_file_path: str = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(data_file_path) as file:
                data = json.load(file)
                return cls(data['words'], data['lang'])
        except FileNotFoundError:
            print(f'File {filename} not found')
            return cls([], 'en')
    

def main():
    data = WordCollection.from_json('words.json')
    print(data)
    