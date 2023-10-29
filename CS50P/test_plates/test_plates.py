from plates import is_valid


def main():
    test_min_max_characters()
    test_starting_with_two_letters()
    test_numbers_in_middle()
    test_first_number_zero()
    test_other_characters()


def test_min_max_characters():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


def test_starting_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("22") == False


def test_numbers_in_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False


def test_other_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("Hello!") == False


if __name__ == "__main__":
    main()
