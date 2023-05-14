import cv2
import numpy as np
import os

alpha = 0

def pre_process_rgb(rgb, x, y):
    x1 = 45
    x2 = 390
    y1 = 80
    y2 = 570
    rgb = rgb[x1:x2,y1:y2,:]    
    rgb = cv2.resize(rgb, (x, y),interpolation = cv2.INTER_LINEAR)               
    return rgb    
    
def process_img(rgb, thermal, out_path):
    rgb = pre_process_rgb(rgb, int(rgb.shape[1]), int(rgb.shape[0]))
    mask = cv2.Laplacian(rgb, cv2.CV_8U, ksize=3)
    mask_inv = cv2.bitwise_not(mask)
    thermal_enhanced = cv2.add(thermal, mask)
    #thermal_enhanced_inv = cv2.bitwise_and(thermal, mask_inv)
    output = cv2.addWeighted(thermal_enhanced, 1, rgb, 0, 0)
    cv2.imwrite(out_path, output)
    return True

dataset_path = "/home/p51pro/UD/Academic/ELEG604/Project/DataSet/"
output_path = "/home/p51pro/UD/Academic/ELEG604/Project/DataSet/repro_msx"

if not os.path.exists(output_path):
    os.mkdir(output_path)
rgb_img_path = os.path.join(dataset_path,"rgb")
thermal_img_path = os.path.join(dataset_path,"thermal")

for file_name in ["FLIR5951.jpg","FLIR6201.jpg","FLIR5763.jpg","FLIR4745.jpg","FLIR5169.jpg","FLIR4575.jpg","FLIR5831.jpg","FLIR4629.jpg"]:
    #print(file_name)
    
    rgb = cv2.imread(os.path.join(rgb_img_path,file_name))
    thermal = cv2.imread(os.path.join(thermal_img_path,file_name))
    file_out_name = os.path.join(output_path,file_name)
    process_img(rgb, thermal, file_out_name)

