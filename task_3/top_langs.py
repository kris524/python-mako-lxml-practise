# Task 5
from mako.template import Template
from lxml import etree

doc = etree.parse("top_langs.xml")

languages = doc.findall("language")


mytemplate = Template(filename="report_template.html")

res = mytemplate.render(languages=languages)

with open("lang_report.html", "w") as f:
    f.write(res)