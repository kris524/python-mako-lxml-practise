# For each port in ports: Get the logicalName,
# description, width of wire Master, direction of that wire and presence

from dataclasses import dataclass
from typing import List
import lxml.etree as etree
from mako.template import Template

doc = etree.parse("CHI_D_RND_rtl.xml")

ns = {"spirit": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"}

logical_names = doc.xpath(
    "//spirit:ports/spirit:port/spirit:logicalName/text()", namespaces=ns
)

desc = doc.xpath("//spirit:ports/spirit:port/spirit:description/text()", namespaces=ns)

presence = doc.xpath("//spirit:onMaster/spirit:presence/text()", namespaces=ns)
direction = doc.xpath("//spirit:onMaster/spirit:direction/text()", namespaces=ns)

master = doc.xpath("//spirit:onMaster", namespaces=ns)

width_res = []
for m in master:
    width = m.xpath("spirit:width/text()", namespaces=ns)  # careful with the xpath here

    w = width[0] if width else "Not Given"

    width_res.append(w)


@dataclass
class PortData:
    logical_names: List[str]
    desc: List[str]
    presence: List[str]
    direction: List[str]
    width_res: List[str]


if __name__ == "__main__":
    port_data = PortData(logical_names, desc, presence, direction, width_res)

    template = Template(filename="template.html")
    res = template.render(port_data=port_data)

    with open("ip_report.html", "w") as f:
        f.write(res)
