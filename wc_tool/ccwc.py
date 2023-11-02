#!/usr/bin/env python3
import argparse

import utilities


def main(args):
    with args.file as file:
        data = file.read()

    line_count = word_count = byte_count = char_count = 0

    if args.bytes:
        byte_count = utilities.count_bytes(data)
    if args.lines:
        line_count = utilities.count_lines(data)
    if args.words:
        word_count = utilities.count_words(data)
    if args.chars:
        char_count = utilities.count_chars(data)

    if all([args.bytes, args.lines, args.words, args.chars]) is False:
        byte_count = utilities.count_bytes(data)
        line_count = utilities.count_lines(data)
        word_count = utilities.count_words(data)
        char_count = utilities.count_chars(data)

    return {
        "line_count": line_count,
        "word_count": word_count,
        "byte_count": byte_count,
        "char_count": char_count,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-m", "--chars", action="store_true", help="Count characters")
    parser.add_argument("file", type=argparse.FileType(mode="rb"))

    args = parser.parse_args()
    result = main(args)

    if args.lines:
        print(f"Line count: {result['line_count']}")
    if args.words:
        print(f"Word count: {result['word_count']}")
    if args.bytes:
        print(f"Byte count: {result['byte_count']}")
    if args.chars:
        print(f"Char count: {result['char_count']}")
    elif not (args.lines or args.words or args.bytes or args.chars):
        # If no option is provided, print all counts
        print(f"Line count: {result['line_count']}")
        print(f"Word count: {result['word_count']}")
        print(f"Byte count: {result['byte_count']}")
        print(f"Char count: {result['char_count']}")
