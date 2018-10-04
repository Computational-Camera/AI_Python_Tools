#borrowed from detection generate coco format annotations, slightly modified and reduced
#Dependency cocoapi and cityscape scripts (need modification, see detection)
#output: invalid contour need to check
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import h5py
import json
import os
import scipy.misc
import sys

import cityscapesscripts.evaluation.instances2dict_with_polygons as cs

import detectron.utils.segms as segms_util
import detectron.utils.boxes as bboxs_util


DATADIR    = "../"
OUTPUTDIR  = "./"

# for Cityscapes
def getLabelID(self, instID):
    if (instID < 1000):
        return instID
    else:
        return int(instID / 1000)

def convert_cityscapes_instance_only(data_dir, out_dir):
    """Convert from cityscapes format to COCO instance seg format - polygons"""
    sets = [
        #'gtFine_val'
         'gtFine_train',
        # 'gtFine_test',

        # 'gtCoarse_train',
        # 'gtCoarse_val',
        # 'gtCoarse_train_extra'
    ]
    ann_dirs = [
        #'gtFine_trainvaltest/gtFine/val'
         'gtFine_trainvaltest/gtFine/train',
        # 'gtFine_trainvaltest/gtFine/test',

        # 'gtCoarse/train',
        # 'gtCoarse/train_extra',
        # 'gtCoarse/val'
    ]
    json_name = 'instancesonly_filtered_%s.json'
    ends_in = '%s_polygons.json'
    img_id = 0
    ann_id = 0
    cat_id = 1
    category_dict = {}

    category_instancesonly = [
        'person',
        'rider',
        'car',
        'truck',
        'bus',
        'caravan',
        'trailer',
        'train',
        'motorcycle',
        'bicycle',
    ]

    for data_set, ann_dir in zip(sets, ann_dirs):
        print('Starting %s' % data_set)
        ann_dict = {}
        images = []
        annotations = []
        ann_dir = os.path.join(data_dir, ann_dir)

        for root, _, files in os.walk(ann_dir):
            for filename in files:
                #print("*******", filename)
                if filename.endswith(ends_in % data_set.split('_')[0]):
                    if len(images) % 50 == 0:
                        print("Processed %s images, %s annotations" % ( len(images), len(annotations)))
                    json_ann = json.load(open(os.path.join(root, filename)))
                    image = {}
                    image['id'] = img_id
                    img_id += 1

                    image['width']  = json_ann['imgWidth']
                    image['height'] = json_ann['imgHeight']
                    image['file_name']     = filename[:-len(ends_in % data_set.split('_')[0])]    + 'leftImg8bit.png'
                    image['seg_file_name'] = filename[:-len(ends_in % data_set.split('_')[0])]+'%s_instanceIds.png' % data_set.split('_')[0]
                    images.append(image)

                    fullname = os.path.join(root, image['seg_file_name'])# instance name
                    objects  = cs.instances2dict_with_polygons([fullname], False)[os.path.abspath(fullname)]
                    #print(fullname)
                    #print(objects)
                    for object_cls in objects:
                        if object_cls not in category_instancesonly:
                            continue  # skip non-instance categories

                        for obj in objects[object_cls]:
                            if obj['contours'] == []:
                                print('Warning: empty contours.')
                                continue  # skip non-instance categories
                            len_p = [len(p) for p in obj['contours']]
                            if min(len_p) <= 4:
                                print('Warning: invalid contours.')
                                continue  # skip non-instance categories

                            ann = {}
                            ann['id'] = ann_id
                            ann_id += 1
                            ann['image_id'] = image['id']
                            ann['segmentation'] = obj['contours']

                            if object_cls not in category_dict:
                                category_dict[object_cls] = cat_id
                                cat_id += 1
                            ann['category_id'] = category_dict[object_cls]
                            ann['iscrowd'] = 0
                            ann['area'] = obj['pixelCount']
                            ann['bbox'] = bboxs_util.xyxy_to_xywh(
                                segms_util.polys_to_boxes(
                                    [ann['segmentation']])).tolist()[0]

                            annotations.append(ann)

        ann_dict['images'] = images
        categories = [{"id": category_dict[name], "name": name} for name in
                      category_dict]
        ann_dict['categories'] = categories
        ann_dict['annotations'] = annotations
        print("Num categories: %s" % len(categories))
        print("Num images: %s" % len(images))
        print("Num annotations: %s" % len(annotations))
        with open(os.path.join(out_dir, json_name % data_set), 'w') as outfile:
                  outfile.write(json.dumps(ann_dict))


if __name__ == '__main__':
    #args = parse_args()
    #if args.dataset == "cityscapes_instance_only":
    convert_cityscapes_instance_only(DATADIR,OUTPUTDIR)
    #else:
    #    print("Dataset not supported: %s" % args.dataset)

