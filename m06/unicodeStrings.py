char = "\U0001F595"
charname = "\N{LATIN SMALL LETTER B WITH DOT BELOW}"
print(char + " " + charname)

import unicodedata as ud
print(ud.name("a"))
print(ud.lookup(ud.name("a")))

def get_by_name(value):
    name = ud.name(value)
    return(ud.lookup(name), name)