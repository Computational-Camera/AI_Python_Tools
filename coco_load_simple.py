    #formatl explaination linke http://cocodataset.org/#format-data
    #load coco annotations file to obtain annotations
    #without using coco API
    import json
    from collections import defaultdict
    annotation_file = "xxx/Dataset/COCO/annotations/instances_train2017.json"
    dataset         = json.load(open(annotation_file, 'r'))
    imgToAnns       = defaultdict(list) #store image_id -> annotation
    anns, imgs = {},  {}
    if 'annotations' in dataset:  # get annotations
        for ann in dataset['annotations']:
            imgToAnns[ann['image_id']].append(ann)
            #print(ann)
            #anns[ann['id']] = ann
    #print(imgToAnns.keys())
    if 'images' in dataset:  # get images name
        for img in dataset['images']:
            imgs[img['id']] = img
            
    ids = list(imgToAnns.keys()) 
    index = 3
    target =  imgToAnns[ids[index]]
    print(ids[index])
    print(imgs[ids[index]]['file_name'])
    #print(target)
    #print(dataset)
    print("===============================")
