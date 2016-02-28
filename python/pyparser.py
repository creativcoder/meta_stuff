import pyparsing as pp
import sys

input_text = '<b>BoldTagElement</b>'

# This is the extended backus naur form for representing context free grammers
# first       ::=  letter | "_"
# letter      ::=  "a" | "b" | ... "z" | "A" | "B" | ... | "Z"
# digit       ::=  "0" | "1" | ... | "9"
# rest        ::=  first | digit
# identifier  ::=  first rest*

WHITESPACE = ' '
BOLD = '<b>'
BOLD_END = '</b>'
CONTENT = 'a-zA-Z' | WHITESPACE
BOLD_TAG = BOLD | CONTENT | BOLD_END

first = pp.Word(pp.alphas+"_",exact=1)
rest = pp.Word(pp.alphanums+"_")
identifier = first+pp.Optional(rest)

testCases = [
# Some valid ones
"a","_b","_2343",
# Some not valid ones
"3dgfre",",","@"
]
