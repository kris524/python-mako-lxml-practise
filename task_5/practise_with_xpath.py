# Question: Extract and Print the Component Details from the IP-XACT file

# Write a Python script to extract and print the vendor, library, 
# name, and version details of the component described in the CHI-D-RND 
# IP-XACT file. For this, you will need to parse the XML file and locate the relevant information.
import lxml.etree as etree


doc = etree.parse("CHI_D_RND_rtl.xml")

ns = {"spirit": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"}


a = doc.xpath("//*[@library]")

via_attributes = doc.xpath("//spirit:busType[@spirit:library]", namespaces=ns)


#TODO: Use a for loop to iterate over the elements, makes it look better
direct_access_vendor = doc.xpath("//spirit:vendor/text()", namespaces=ns)
direct_access_library = doc.xpath("//spirit:library/text()", namespaces=ns)
direct_access_version = doc.xpath("//spirit:version/text()", namespaces=ns)
direct_access_name = doc.xpath("//spirit:name/text()", namespaces=ns)


logicalName = doc.xpath("//spirit:logicalName", namespaces=ns)

if __name__ == "__main__":
    print(via_attributes[0])

    print(direct_access_vendor)
    print(direct_access_library)
    print(direct_access_version)
    print(direct_access_name)

    print(logicalName[0].text)