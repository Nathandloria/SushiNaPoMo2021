import src.pos_tokenizer as tokenizer

def test_tokenizer():
    pos, words = tokenizer.pos_tokenize("hello world, hows it going?")
    assert not len(words) == 0