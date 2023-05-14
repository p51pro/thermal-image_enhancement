# Required Libraries
import cv2
import numpy as np
import os
  
mypath = "/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/val/msx"
mypath_out = "/home/p51pro/UD/Academic/ELEG604/Project/DataSet/postprocessed_dataset/val/msx_orig_size"

for file_name in os.listdir(mypath):
    path = os.path.join(mypath, file_name)
    img = cv2.imread(path)
    
    resized_dimensions = (160, 120)
    
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)
  
    new_file_name = os.path.join(mypath_out,file_name)
    print(new_file_name)
    cv2.imwrite(new_file_name, resized_image)
  
