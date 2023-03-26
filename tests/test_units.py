import pytest
from src.main import english_to_morse_code

def test_english_to_morse_code():
    test_cases = [
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("SOS", "... --- ..."),
        ("abc123", ".- -... -.-. .---- ..--- ...--"),
        ("fun project", "..-. ..- -. / .--. .-. --- .--- . -.-. -"),
    ]

    for text, expected in test_cases:
        assert english_to_morse_code(text) == expected

def test_english_to_morse_code_special_chars():
    test_cases = [
        ("!?.,", "-.-.-- ..--.. .-.-.- --..--"),
        ("@$", ".--.-. ...-..-")
    ]

    for text, expected in test_cases:
        assert english_to_morse_code(text) == expected

if __name__ == "__main__":
    pytest.main()
