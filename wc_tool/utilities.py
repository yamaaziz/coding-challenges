def count_bytes(data):
    return len(data)


def count_lines(data):
    return data.count(b"\n")


def count_words(data):
    return len(data.split())


def count_chars(data):
    return len(data.decode("utf-8"))
