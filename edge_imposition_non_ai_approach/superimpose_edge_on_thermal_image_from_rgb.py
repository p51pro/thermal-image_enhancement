import cv2
import numpy as np
import os

alpha = 0


def pre_process_rgb(rgb, x, y):
    x1 = 45   #45
    x2 = 390  #390
    y1 = 80   #80
    y2 = 570  #570
    rgb = rgb[x1:x2,y1:y2,:]    
    rgb = cv2.resize(rgb, (x, y),interpolation = cv2.INTER_LINEAR)               
    return rgb    
    
def process_img(rgb, thermal, out_path):
    rgb = pre_process_rgb(rgb, int(rgb.shape[1]), int(rgb.shape[0]))    
    mask = cv2.Laplacian(rgb, cv2.CV_8U, ksize=3)

    mask_inv = cv2.bitwise_not(mask)
    thermal_enhanced = cv2.add(thermal, mask)
    thermal_enhanced_inv = cv2.bitwise_and(thermal, mask_inv)
    
    #gamma = 1/2
    #gamma_corrected = np.array(255*(rgb / 255) ** gamma, dtype = 'uint8')
    
    #contrast=5
    #brightness=2
    #rgb = cv2.addWeighted( rgb, contrast, rgb, 0, brightness)
    gamma = 3
    gamma_corrected = np.array(255*(rgb / 255) ** gamma, dtype = 'uint8')
    
    output = cv2.addWeighted(thermal_enhanced_inv, 0.7, gamma_corrected, 0.4, 0)
    
    cv2.imwrite(out_path, output)
    return True

dataset_path = "/home/p51pro/UD/Academic/ELEG604/Project/thermal-image_enhancement/edge_imposition_non_ai_approach/testing/"
output_path = "/home/p51pro/UD/Academic/ELEG604/Project/thermal-image_enhancement/edge_imposition_non_ai_approach/testing/repro_msx"

if not os.path.exists(output_path):
    os.mkdir(output_path)
rgb_img_path = os.path.join(dataset_path,"rgb")
thermal_img_path = os.path.join(dataset_path,"thermal")

for file_name in os.listdir(thermal_img_path):
    rgb = cv2.imread(os.path.join(rgb_img_path,file_name))
    thermal = cv2.imread(os.path.join(thermal_img_path,file_name))
    file_out_name = os.path.join(output_path,file_name)
    process_img(rgb, thermal, file_out_name)

