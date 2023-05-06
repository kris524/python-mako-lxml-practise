# Task 5
from mako.template import Template
from lxml import etree

doc = etree.parse("top_langs.xml")

language = doc.findall("language")

print(language)



with open("output3.html", "w") as f:
    f.write(res)