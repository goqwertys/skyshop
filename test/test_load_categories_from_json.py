import json
from unittest.mock import mock_open, patch

from src.utils import load_categories_from_json


def test_successful_load():
    json_data = [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                }
            ]
        }
    ]
    mock_open_file = mock_open(read_data=json.dumps(json_data))
    with patch("builtins.open", mock_open_file):
        categories = load_categories_from_json("fake_path.json")
        assert len(categories) == 1
        assert categories[0].name == "Смартфоны"
        assert len(categories[0].products) == 1
        assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"


def test_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        categories = load_categories_from_json('nonexistent_file.json')
        assert categories == []


def test_json_decode_error():
    mock_open_file = mock_open(read_data='invalid json')
    with patch('builtins.open', mock_open_file):
        categories = load_categories_from_json('fake_path.json')
        assert categories == []


def test_other_exceptions():
    with patch('builtins.open', side_effect=Exception("Some error")):
        categories = load_categories_from_json('fake_path.json')
        assert categories == []
