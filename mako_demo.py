from mako.template import Template


# TASK 1: Create an HTML table from a list of dictionaries in Python.
# Each dictionary represents a row in the table, and the keys
# represent the column names. The table should have alternating
# row colors and should include a header row.

list_of_cols = ["dog_name", "age", "height"]

list_of_dicts = [
    {"dog_name": "vsv", "age": 12, "height": 3},
    {"dog_name": "ger", "age": 5, "height": 7},
]

mytemplate = Template(filename="table.html")

result = mytemplate.render(list_of_cols=list_of_cols, list_of_dicts=list_of_dicts)

with open("output.html", "w") as f:
    f.write(result)
