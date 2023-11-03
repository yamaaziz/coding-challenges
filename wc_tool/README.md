# wc Tool

## Description
wc is a utility tool that displays the number of lines, words, characters, and bytes contained in an input file.

![Alt text](demo.svg)
## Setup
```
cd coding-challenges/
source .env
pip install -r wc_tool/requirements.txt
```
## Tests
`pytest`
## Usage
```
python wc_tool/ccwc.py --bytes wc_tool/test.txt
python wc_tool/ccwc.py --lines wc_tool/test.txt
python wc_tool/ccwc.py --words wc_tool/test.txt
python wc_tool/ccwc.py --chars wc_tool/test.txt
python wc_tool/ccwc.py wc_tool/test.txt
```

## Future work
- Create an installable package
- Refactor to use binary streams
- Refactor to read from standard input