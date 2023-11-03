def test_main_with_args(sample_args, capsys):
    from wc_tool import ccwc

    result = ccwc.main(sample_args)

    captured = capsys.readouterr()
    output = captured.out.splitlines()

    print("capsys", capsys.readouterr())
    print("result", result)
    print("captured", captured)
    print("output", output)

    assert result == {
        "line_count": 1,
        "word_count": 7,
        "byte_count": 35,
        "char_count": 35,
    }

    assert "Line count: 1" in output
    assert "Word count: 7" in output
    assert "Byte count: 35" in output
    assert "Char count: 35" in output


def test_main_without_args(sample_args, capsys):
    from wc_tool import ccwc

    # Remove all count options (bytes, lines, words, chars)
    sample_args.bytes = False
    sample_args.lines = False
    sample_args.words = False
    sample_args.chars = False

    result = ccwc.main(sample_args)

    captured = capsys.readouterr()
    output = captured.out.splitlines()

    assert result == {
        "line_count": 1,
        "word_count": 7,
        "byte_count": 35,
        "char_count": 35,
    }

    # Expecting all counts to be printed
    assert "Line count: 1" in output
    assert "Word count: 7" in output
    assert "Byte count: 35" in output
    assert "Char count: 35" in output
