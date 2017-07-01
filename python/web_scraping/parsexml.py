import xml.etree.ElementTree as ET

data = '''
<person>
   <name>Chuck</name>
   <phone type="intl">
         +1 312 731 6415
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) #parses the xml string and creates an object. Then using this object to look for things in xml
print 'Name:',tree.find('name').text # find attribute name and then get the text. get the tag "name"
print 'Attr:',tree.find('email').get('hide') # in email tag get the attribute for "hide"
