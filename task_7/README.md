IP-XACT is an XML schema for defining and describing electronic components and systems. A common use of IP-XACT files is to describe components like CPUs, memories, and peripherals in a system-on-chip design. Each component in an IP-XACT file can have properties like name, vendor, library, version, bus interfaces, memory maps, address spaces, and more.

Here's a basic outline of how you might do this:

1. Use lxml to parse the IP-XACT file and get the root element of the XML tree.

2. Use XPath to select all spirit:component elements in the tree (assuming that the spirit namespace prefix is used in your IP-XACT file).

3. For each spirit:component element, use XPath and the get() method to extract information about the component, such as its name, vendor, library, version, etc.

4. Define a Mako template for the report. This could be a simple text format, or you could generate an HTML report for viewing in a web browser. Use ${} placeholders in the template for the information you want to include about each component.

5. For each spirit:component element, render the Mako template with the information you extracted from the element.

6. Write the rendered templates to a file to create the report.

Remember that XPath expressions in lxml need to include namespace prefixes, and you need to provide a dictionary of namespace mappings. You can usually find the namespace URI for the spirit prefix at the top of the IP-XACT file, in the xmlns:spirit attribute.