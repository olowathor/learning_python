'''
identifiers:
\d - any number
\D - anything, but a number
\s - space
\S - anything, but a space
\w - any character
\W - anything, but a character
. - any character, except for a newline
\b - whitespace around words
\. a period

modifiers:
{1,3} - expecting from 1 to three
+ - match one or more
? - match 0 or one
* - match 0 or more
$ - match end of a string
^ - match the beginning of a string
| - either or
[] - range or "variance" [1-5a-qA-Z] example: 4bT, 1cG, 2pD
{x} - expecting "x" amount

whitespace characters:
\n newline
\s space
\t tab
\e escape
\f form feed
\r return


'''
import re

example_string = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 57, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', example_string)
names = re.findall(r'[A-Z][a-z]*', example_string)

print(dict(zip(names,ages)))

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics', 'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)

respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

[print(eachP) for eachP in paragraphs]




