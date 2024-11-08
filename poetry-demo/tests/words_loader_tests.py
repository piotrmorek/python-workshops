# tests/test_word_collection.py
from poetry_demo.translate_text import WordCollection
from unittest.mock import mock_open, patch

class TestWordCollection:
    
    @patch('builtins.open', new_callable=mock_open, read_data='{"words":["hello","world"], "lang": "en" }')
    def test_json_file_should_be_load_and_parsed(self, _):
        data = WordCollection.from_json('fake_file.json')
        assert data.words == ['hello', 'world']
        assert data.lang == 'en'