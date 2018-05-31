import json
from pprint import pprint

with open('valid_anno.json') as json_data: 
    d = json.load(json_data)
print(type(d))
pprint(d)
#info
#images
#licenses
#annotations
#categories
"""
print ("total length is ", len(d['images']), len( d.items()))
for key, value in d.items():
    print key
    print d['info']
    print d['images'][0] 
    print d['licenses'][0] 
"""
#pprint (d['annotations'])
#print d['categories']   # totally 81 for coco     
#for ele in d.values():
#    print(ele)
#    if isinstance(ele,dict):
#       for k, v in ele.items():
#           print(k,' ',v)
