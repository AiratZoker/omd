from unittest.mock import patch
from what_is_year_now import what_is_year_now


def test_what_is_year_now_ymd():
    with patch('what_is_year_now.json.load') as mocked_load:
        mocked_load.return_value = {"currentDateTime": "2023-11-05"}
        assert what_is_year_now() == 2023
        mocked_load.assert_called_once()


def test_what_is_year_now_dmy():
    with patch('what_is_year_now.json.load') as mocked_load:
        mocked_load.return_value = {"currentDateTime": "05.11.2023"}
        assert what_is_year_now() == 2023
        mocked_load.assert_called_once()


def test_what_is_year_now_exp():
    with patch('what_is_year_now.json.load') as mocked_load:
        mocked_load.return_value = {"currentDateTime": "05@11@2023"}
        try:
            what_is_year_now() == 2023
        except ValueError as e:
            print(f"{e}")
        mocked_load.assert_called_once()
