import numpy as np

#find index of arrays that has same tag
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

#create the unique name list from a list
label_names = list(set(labels))

#sort the list in alphabet order
label_names_sorted = sorted(label_names)

#read a list from CSV
f = pd.read_csv('./data/sample_submission.csv')
image_id = f['id'].tolist()
