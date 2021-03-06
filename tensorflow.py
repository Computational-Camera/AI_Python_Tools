#check the current device being used cpu or gpu
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

#Memory usage, by default, the GPU memory will be all occpupied
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
set_session(tf.Session(config=config))

#object detection example
import numpy as np
import os
import sys
import time
import tensorflow as tf
from collections import defaultdict
from io import StringIO
from PIL import Image
import cv2
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from object_detection.utils import ops as utils_ops
print(tf.__version__)
from utils import label_map_util
from utils import visualization_utils as vis_util

MODEL_NAME = './download_model/faster_rcnn_inception_v2_coco_2018_01_28'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=128, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

def load_image_into_numpy_array(image):
  im_height, im_width, channel = image.shape
  print(im_width, im_height, channel)
  return np.array(image).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def run_inference_for_images(graph):
  with graph.as_default():
    with tf.Session() as sess:
      # Get handles to input and output tensors
      ops = tf.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
      ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
              tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes,10024,768)#
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')
      
      cap = cv2.VideoCapture('./VID_20180412_201741.mp4')
      #Capturing video from webcam:
      #cap = cv2.VideoCapture(0)
      currentFrame = 0
  
      while(cap.isOpened()):
          # Capture frame-by-frame
          ret, frame = cap.read()
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
          if ret == True:
              currentFrame += 1
              image_np = load_image_into_numpy_array(frame)
		      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
              image_np_expanded = np.expand_dims(image_np, axis=0)
		      # Actual detection.
              start = time.time()
              output_dict = sess.run(tensor_dict, feed_dict={image_tensor: np.expand_dims(image_np, 0)})
              end = time.time()
              print(end - start)
		      # all outputs are float32 numpy arrays, so convert types as appropriate
              output_dict['num_detections']    = int(output_dict['num_detections'][0])
              output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
              output_dict['detection_boxes']   = output_dict['detection_boxes'][0]
              output_dict['detection_scores']  = output_dict['detection_scores'][0]
              if 'detection_masks' in output_dict:
                output_dict['detection_masks'] = output_dict['detection_masks'][0]
		      # Visualization of the results of a detection.
              vis_util.visualize_boxes_and_labels_on_image_array( image_np, output_dict['detection_boxes'],
			      output_dict['detection_classes'], output_dict['detection_scores'], category_index,
			      instance_masks=output_dict.get('detection_masks'), use_normalized_coordinates=True, line_thickness=8)
              cv2.imshow('frame',image_np)
          else: 
            break
      cap.release()
      cv2.destroyAllWindows()
print('finish')
if __name__ == '__main__':
    run_inference_for_images(detection_graph)


