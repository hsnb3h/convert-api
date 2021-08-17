import base64
from pydocx import PyDocX
import fileinput
import zipper
from bs4 import BeautifulSoup
import re


def text_to_base64(text):
    encodedBytes = base64.b64encode(text.encode('utf-8'))
    return encodedBytes


def base64_to_text(text):
    decoded = base64.b64decode(text).decode('utf-8')
    return decoded





Html = PyDocX.to_html('Docs/d1-png.docx')
f = open('./HTML/from-docx.html', 'w', encoding='utf-8')
f.write(Html)
f.close()
File = open('./HTML/from-docx.html', 'a')



with fileinput.FileInput('./HTML/from-docx.html', inplace=True) as file:
    for line in file:
        print(line.replace('<html>', '<html lang="ar" dir="rtl">'))



File.close()
File = open('./HTML/from-docx.html', 'r')
codeBase = File.read()
File.close()
File = open('./HTML/from-docx.html', 'w')
soup = BeautifulSoup(codeBase, 'html.parser')
output = re.sub('<span class="pydocx-center".+?</table>','',codeBase,flags=re.DOTALL)


response = BeautifulSoup(output, 'html.parser')
for script in response('hr'):
    script.decompose()
output = str(response.prettify())
File.write(str(output))
File.close()

f = open('./HTML/from-docx.html', 'r')
codebase = f.read()
f.close()
questions = []
text = codebase.split('IDENTIFIER')
text.pop(0)
encoded_list = []
formatting = '<html lang="ar" dir="rtl"><head><meta charset="utf-8" /><style>.pydocx-caps {text-transform:uppercase}.pydocx-center {text-align:center}.pydocx-comment {color:blue}.pydocx-delete {color:red;text-decoration:line-through}.pydocx-hidden {visibility:hidden}.pydocx-insert {color:green}.pydocx-left {text-align:left}.pydocx-list-style-type-cardinalText {list-style-type:decimal}.pydocx-list-style-type-decimal {list-style-type:decimal}.pydocx-list-style-type-decimalEnclosedCircle {list-style-type:decimal}.pydocx-list-style-type-decimalEnclosedFullstop {list-style-type:decimal}.pydocx-list-style-type-decimalEnclosedParen {list-style-type:decimal}.pydocx-list-style-type-decimalZero {list-style-type:decimal-leading-zero}.pydocx-list-style-type-lowerLetter {list-style-type:lower-alpha}.pydocx-list-style-type-lowerRoman {list-style-type:lower-roman}.pydocx-list-style-type-none {list-style-type:none}.pydocx-list-style-type-ordinalText {list-style-type:decimal}.pydocx-list-style-type-upperLetter {list-style-type:upper-alpha}.pydocx-list-style-type-upperRoman {list-style-type:upper-roman}.pydocx-right {text-align:right}.pydocx-small-caps {font-variant:small-caps}.pydocx-strike {text-decoration:line-through}.pydocx-tab {display:inline-block;width:4em}.pydocx-underline {text-decoration:underline}body {margin:0px auto;width:49.61em}</style></head><body><p><span class="pydocx-underline">'
for i in range(len(text)):
    text[i] = formatting + text[i] + '</body></html>'
    encoded_list.append(text[i])

data = {}
for i, value in enumerate(encoded_list):
    data[i+1] = value

for i in range(len(data)):
    print(data.get(i+1))




# data = {}
# for i, value in enumerate(encoded_list):
#     data[i+1] = value

