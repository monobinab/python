import json  #json is nested lists and dictionaries
input = '''[
   { "id" : "001",
     "x"  : "2",
     "name" : "Chuck"
   } ,
   {  "id" : "009",
      "x"  : "7",
      "name"  : "Chuck"
   }
]'''

info = json.loads(input)  # loads is load s for string. info is a list. This step is deserialization
print 'User count:', len(info)
for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']

###########################################################################


#########################################################################################

#######################################################################################
