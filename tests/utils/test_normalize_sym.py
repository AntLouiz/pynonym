import unicodedata


def test_replace_non_ascii_words():
    text_with_non_ascii = 'Maçã'
    text_with_non_ascii_words_replaced = 'Maca'

    nfkd_form = unicodedata.normalize('NFKD', text_with_non_ascii)
    only_ascii_word = nfkd_form.encode('ASCII', 'ignore')

    decoded_only_ascii_word = only_ascii_word.decode('UTF-8')

    assert decoded_only_ascii_word == text_with_non_ascii_words_replaced
