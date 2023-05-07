from lxml import etree
from mako.template import Template
# TASK 4
doc = etree.parse("movies.xml")

movies = doc.findall("movie")
print(movies)

list_of_cols = ["title", "director", "year", "rating"]

mytemplate = Template(filename="movie_table.html")

res = mytemplate.render(list_of_cols=list_of_cols, movies=movies)

with open("output2.html", "w") as f:
    f.write(res)